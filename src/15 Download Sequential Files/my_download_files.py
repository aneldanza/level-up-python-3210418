import re
from urllib.request import urlretrieve, Request, urlopen, HTTPError
import urllib.parse
import os

def get_next_seq(seq):
  next = str(int(seq) + 1)
  return next.zfill(len(seq))


def my_download_files(first_file_path, output_dir_name):
  if not os.path.isdir(output_dir_name):
    os.mkdir(output_dir_name)

  parsed_url = urllib.parse.urlparse(first_file_path)
  path_parts = list(parsed_url.path.split('/'))

  data = get_info(path_parts, parsed_url)
  filename = path_parts[data["filename_idx"]]
  url = first_file_path
  seq = data["starting_num"]

  while is_url_reacheable(url):
    urlretrieve(url, f'{output_dir_name}/{filename}')
    next_seq = get_next_seq(seq)
    new_path = get_path_with_new_sequence(seq, filename, path_parts, data["filename_idx"])
    url = urllib.parse.urlunparse(parsed_url._replace(path=new_path))
    seq = next_seq
    filename = new_path.split('/')[-1]
    


def get_info(path_parts, parsed_url):
  i = len(path_parts) - 1

  while i >= 0:
    filename = path_parts[i]
    numbers = re.findall(r"\d+", filename)

    for seq in numbers:
      new_path = get_path_with_new_sequence(seq, filename, path_parts, i)
      
      new_url = urllib.parse.urlunparse(parsed_url._replace(path=new_path))

      if is_url_reacheable(new_url):
        return {"filename_idx": i, "starting_num": seq}
    
    i =- 1



def get_path_with_new_sequence(seq, part, parts, i):
  next_str = get_next_seq(seq)
  filename = part.replace(seq, next_str)
  new_parts = list(parts.copy())
  new_parts[i] = filename
  new_path = '/'.join(new_parts)
  return new_path
  

def is_url_reacheable(url):
  request = Request(url)
  request.get_method = lambda: 'HEAD'

  try:
    urlopen(request)
    return True
  except HTTPError:
    return False


my_download_files('http://699340.youcanlearnit.net/image001.jpg', './images')
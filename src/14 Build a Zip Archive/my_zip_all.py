
import pathlib
import zipfile

def my_zip_all(path, extensions, output_path):
  
  directory = pathlib.Path(path)

  with zipfile.ZipFile(output_path, mode='w') as archive:
    for file_path in directory.rglob("*"):

      if file_path.suffix in extensions:
        archive.write(file_path, arcname=file_path.relative_to(directory))
  

my_zip_all('my_stuff', ['.jpg', '.txt'], 'my_stuff.zip')
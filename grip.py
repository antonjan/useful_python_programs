import gzip import shutil
 def compress_file(input_file, output_file):
   with open(input_file, 'rb') as f_in:
     With gzip.open(output_file, 'wb') as f_out:
      shutil.copyfileobj(f_in, f_out)
 #  usage
input_filename = 'clcoding.txt
output_filename = 'clcoding.txt.gz
compress_file(input_filename, output_filename)

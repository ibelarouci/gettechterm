import glob
import shutil
from  pdftotxtFOF import convert_pdftotex

# search all PDF files inside a specific folder and copy it in source files folder

dir_path = r'./fp/**/*.pdf'
i=0
for file in glob.glob(dir_path, recursive=True):
    
    src=file
    i=i+1
    dst="./sourcefiles/fp"+str(i).zfill(4)+file.replace(" ", "").replace("/",".")[8:16]+".pdf"
    print(dst)
    shutil.copy(src,dst)
 
import glob
import shutil
from  pdftotxtFOF import convert_pdftotex


dir_path = r'./sourcefiles/**/*.pdf'
i=0
for file in glob.glob(dir_path, recursive=True):
    
    src=file
    i=i+1
    print(i)
    dst=file.replace("pdf", "txt").replace("sourcefiles",'txtfiles')
    print(dst)
    convert_pdftotex(src,dst)
    




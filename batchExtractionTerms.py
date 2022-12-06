import glob
from extractTermsFOF import extractTechTerm





dir_path = r'./txtfiles/**/*.txt'
i=0
lines="branch;term;nb_occu\n"
for file in glob.glob(dir_path, recursive=True):
    i=i+1
    print(file)
    lines=lines+extractTechTerm(file)

filename='lexicon'

text_file = open(filename+".csv", "w")
for line in lines:
   text_file.write(line)
text_file.close()








"""plurals = ['caresses', 'flies', 'dies', 'mules', 'geese', 'mice', 'bars', 'foos',
           'families', 'dogs', 'child', 'wolves']

singles = [singularize(plural) for plural in plurals]
print(singles)
"""

  
    
import pdftotxtFOF

def convert_pdftotex (src,dst):
# Load your PDF
    with open(src, "rb") as f:
        pdf = pdftotxtFOF.PDF(f)
        #print(pdf[0])
        words=[]
        for page in pdf:
            words=words+page.split()
        
        #print(words)

    text_file = open(dst, "w")
    for word in words:
        text_file.write(word + " ")
    text_file.close()
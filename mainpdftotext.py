import pdftotext

# Load your PDF
with open("./INT 0703/pE.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)
    print(pdf[0])
    words=[]
    for page in pdf:
        words=words+page.split()
    
    #print(words)

text_file = open("list.txt", "w")
for word in words:
    text_file.write(word + " ")
text_file.close()
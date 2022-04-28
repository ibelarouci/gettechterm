import PyPDF2
fhandle = open(r'./INT 0703/PlanE.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(fhandle)
pagehandle = pdfReader.getPage(0)
print(pagehandle.extractText())
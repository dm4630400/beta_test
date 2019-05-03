# -*- coding: utf-8 -*-
import glob, os, time, sys
from PyPDF2 import PdfFileWriter, PdfFileReader

def split_by_template(lst,template):
        chunks,count = [],0
        for size in template:
                chunks.append([lst[i+count] for i in range(size)])
                count += size
        return chunks

def split_equal(lst,n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]
    
def split_pdf(document_name,pages_list_to_cut):
        input_doc = PdfFileReader(open(document_name, "rb"))
        print(pages_list_to_cut)
        for i in pages_list_to_cut:
                print("i - ",i)
                output_doc = PdfFileWriter()
                for j in i:
                        output_doc.addPage(input_doc.getPage(j-1))
                        print("j - ",j)
                with open(base_path+"document-page%s.pdf" % str(i), "wb") as outputStream:
                        output_doc.write(outputStream)

def print_pdf():
        print('---------- Printing -------------')
        documents_for_printing = sorted(glob.glob(base_path+"document-page*.pdf"),reverse=False)
        print(documents_for_printing)
        for file in documents_for_printing+documents_for_printing[1:]:
                print(file)
                lts = os.startfile(file, "print")
        print('---------- Removing -------------')
        time.sleep(30)
        while documents_for_printing:
                try:
                        os.remove(documents_for_printing[0])
                        documents_for_printing.pop(0)
                except PermissionError:
                        time.sleep(1)




base_path = "D:\\PRINT\\"
document_input = max(glob.glob(base_path+"Order*.pdf"), key=os.path.getctime)
pdf = PdfFileReader(open(document_input,'rb'))
print(pdf.getNumPages())
total_pdf_pages = pdf.getNumPages()
list_of_pdf_pages = list(range(1,total_pdf_pages+1))
print('list of all pdf pages:',list_of_pdf_pages)
template = [1,2]
parts = None
for equal_part in split_equal(list_of_pdf_pages,sum(template)):
        try:
                print(equal_part)
                unequal_parts = split_by_template(equal_part,template)
                print(unequal_parts)
                split_pdf(document_input,unequal_parts)
                print_pdf()
        except IndexError:
                print('Thats enought!')













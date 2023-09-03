'''This code is going to reduce the PDF size
To-do list in order:
1.install pdfplumber
2.Open pdf file
3.Find the desired page
3.1.Find the table on the page
4.Print the values in the table'''
# AmirmohammadVarmaghani - 8/27/2023 - 1402/06/05
import pdfplumber
inputPDF = pdfplumber.open("Sample pdf.pdf")#باز کردن پی دی اف
desiredpage = inputPDF.pages[25]#یافتن صفحه ای که می خواهیم جدول موجود در آن صفحه را ببینیم
ValuesInTheTable = desiredpage.extract_table()#جدا کردن مقادیر موجود در جدول
print("Values in the table are:\n")
print(ValuesInTheTable )#چاپ مقادیر موجود در جدول

import pikepdf

old_pdf = pikepdf.Pdf.open("Python Programming Internship Project 3.pdf")

no_extract = pikepdf.Permissions(extract=False)

old_pdf.save("newfile.pdf", encryption=pikepdf.Encryption(user="391753", owner="Sachin", allow=no_extract))
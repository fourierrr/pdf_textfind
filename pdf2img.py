# from pdf2image import convert_from_path

# pdf_name = "guizhou2012.pdf"
# jpg_name =pdf_name[:-4]

# pages = convert_from_path("guizhou2012.pdf",first_page=1,last_page=10)
# for page in pages:
#     i=1
#     page.save("pic/"+jpg_name+str(i)+'.jpg', 'JPEG')
    # i=i+1

from pdf2image import convert_from_path
convert_from_path('guizhou2012.pdf', 500, "pic",fmt="JPEG",output_file="2012",thread_count=4)
print("finish")
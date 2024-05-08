import pdf2image
import os

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file)


def return_img_info(file):
    try:
        text = pytesseract.image_to_string(file)
        return text
    except Exception as e:
        print(e)
        return ''


def return_pdf_info(pdf_file):
    try:
        paragraph=[]
        images = pdf_to_img(pdf_file)
        for pg, img in enumerate(images):
            paragraph.append(return_img_info(img))

        return ' '.join(paragraph)
    except Exception as e:
       print(e)
       return ''



def isImageOrPdf(fileName):
    file_extension = os.path.splitext(fileName)[1].lower()
     
    is_image = file_extension  in ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff']
    is_pdf = file_extension in '.pdf'
    
    if is_image:
        return 'image'
    elif is_pdf:
        return 'pdf'
    else:
        ''

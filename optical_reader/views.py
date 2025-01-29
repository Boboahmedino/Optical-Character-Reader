import os
import pytesseract
from PIL import Image
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Ensure Tesseract OCR path is set (Windows users only)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def upload_image(request):
    extracted_text = None
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']

        fs = FileSystemStorage()
        file_path = fs.save(image_file.name, image_file)
        file_url = fs.path(file_path)
        
        # Process image with Tesseract OCR
        extracted_text = pytesseract.image_to_string(Image.open(file_url))
        
        # Delete the uploaded file after processing
        os.remove(file_url)
    
    return render(request, 'reader.html', {'text': extracted_text})


import fitz 

def upload_pdf(request):
    extracted_text = None
    if request.method == 'POST' and request.FILES['pdf']:
        pdf_file = request.FILES['pdf']
        
        fs = FileSystemStorage()
        file_path = fs.save(pdf_file.name, pdf_file)
        file_url = fs.path(file_path)
        
        # Open the PDF file using PyMuPDF
        pdf_document = fitz.open(file_url)
        extracted_text = ""
        
        # Iterate through each page in the PDF
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap()
            
            # Save the page as an image
            image_path = f"page_{page_num + 1}.png"
            pix.save(image_path)
            
            # Extract text from the image using Tesseract OCR
            extracted_text += pytesseract.image_to_string(Image.open(image_path)) + "\n"
            
            # Delete the temporary image file
            os.remove(image_path)
        
        # Close the PDF document
        pdf_document.close()
        
        # Delete the uploaded PDF file after processing
        os.remove(file_url)
    
    return render(request, 'reader.html', {'text': extracted_text})
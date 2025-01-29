# Optical Character Reader
---

## Overview
OCR Reader is a Django-based web application that extracts text from images and PDF files using Tesseract OCR. The application provides a user-friendly interface with Bootstrap and Font Awesome icons, ensuring a seamless and visually appealing experience.
---

## Features
- Upload and process image files (JPEG, PNG, etc.) to extract text.
- Upload and process multi-page PDF files for text extraction.
- User-friendly UI with Bootstrap 5 and Font Awesome icons.
- Automatic file management (temporary file deletion after processing).
- Python-based backend leveraging Django and Tesseract OCR.
---

## Technologies Used
- **Frontend:** HTML, CSS (Bootstrap 5), Font Awesome
- **Backend:** Django, Python
- **OCR Engine:** Tesseract OCR
- **PDF Processing:** PyMuPDF (Fitz)
---

## Installation
---

### Prerequisites
Ensure you have the following installed:
- Python 3.12+
- Django 5.1+
- Tesseract OCR ([Download Here](https://github.com/UB-Mannheim/tesseract/wiki))
- PyMuPDF (Fitz)
---

### Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/Boboahmedino/Optical-Character-Reader.git
   cd ocr
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run migrations and start the server:
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```
5. Open your browser and visit `http://127.0.0.1:8000/` to use the application.

## Usage
1. Upload an image file (JPEG, PNG) or a PDF file.
2. Click the **Extract Image** or **Extract PDF** button.
3. Extracted text will be displayed on the screen.

## File Structure
```
ocr/
│-- manage.py
│-- optical_reader/
│   │-- settings.py
│   │-- urls.py
│   │-- views.py
│-- templates/
│   │-- reader.html
│-- requirements.txt
```
---

## Author
Olaneye Ahmed Oladapo


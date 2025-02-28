# 🖹 Optical Character Reader (OCR)  
_A Django-based web application for extracting text from images and PDFs using Tesseract OCR._

---

## 🚀 Overview  
**OCR Reader** is a **Django**-powered web application that leverages **Tesseract OCR** to extract text from images and multi-page PDF files. The application provides an intuitive **Bootstrap 5** interface with **Font Awesome** icons, ensuring a smooth and visually appealing user experience.

---

## ✨ Features  
✔️ Upload and process **image files** (`JPEG`, `PNG`, etc.) for text extraction.  
✔️ Upload and process **multi-page PDF files** for text recognition.  
✔️ **User-friendly UI** with Bootstrap 5 and Font Awesome icons.  
✔️ **Automatic file management** (temporary file deletion after processing).  
✔️ Powered by **Python, Django, and Tesseract OCR** for robust text extraction.  

---

## 🛠️ Technologies Used  
| **Technology**   | **Description** |
|-----------------|---------------|
| **Frontend**   | HTML, CSS (Bootstrap 5), Font Awesome |
| **Backend**    | Django, Python |
| **OCR Engine** | Tesseract OCR |
| **PDF Handling** | PyMuPDF (Fitz) |

---

## 🔧 Installation  

### ✅ Prerequisites  
Ensure you have the following installed before proceeding:  
- **Python 3.12+**  
- **Django 5.1+**  
- **Tesseract OCR** ([Download Here](https://github.com/UB-Mannheim/tesseract/wiki))  
- **PyMuPDF (Fitz)**  

---

### 📌 Setup Instructions  

1️⃣ **Clone the repository**  
```sh
git clone https://github.com/Boboahmedino/Optical-Character-Reader.git
cd Optical-Character-Reader
```

2️⃣ **Create a virtual environment & activate it**  
```sh
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on macOS/Linux:
source venv/bin/activate
```

3️⃣ **Install dependencies**  
```sh
pip install -r requirements.txt
```

4️⃣ **Run migrations & start the server**  
```sh
python manage.py migrate
python manage.py runserver
```

5️⃣ **Access the application**  
Open your browser and visit:  
🔗 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**  

---

## 🎯 Usage  

1️⃣ **Upload** an image (`JPEG`, `PNG`) or a PDF file.  
2️⃣ Click **Extract Image** or **Extract PDF**.  
3️⃣ The extracted text will be displayed on the screen.  

---

## 📁 Project Structure  
```plaintext
Optical-Character-Reader/
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

## 👤 Author  
**Olaneye Ahmed Oladapo**  
🔗 GitHub: [Boboahmedino](https://github.com/Boboahmedino)  
🔗 LinkedIn: [Olaneye Ahmed Oladapo](https://www.linkedin.com/in/olaneye/)  

---

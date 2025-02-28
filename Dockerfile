FROM python:3.11

# Install system dependencies
RUN apt-get update && apt-get install -y tesseract-ocr

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (Render uses 10000 by default)
EXPOSE 10000

# Run the Django application
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "optical_reader.wsgi:application"]

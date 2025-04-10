FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Run Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
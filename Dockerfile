# Starta från Python 3.11
FROM python:3.11-slim

# Sätt arbetsmappen
WORKDIR /app

# Kopiera alla filer till containern
COPY . .

# Installera dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Kör appen
CMD ["python", "app.py"]
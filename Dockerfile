# Get the Fast API image with Python version 3.7
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Create the directory for the container
WORKDIR /abs_sum
COPY requirements.txt ./requirements.txt

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the modules
COPY ./api /abs_sum/api
COPY ./summarizer /abs_sum/summarizer

# Move to API directory
WORKDIR /abs_sum/api

# Run by specifying the host and port
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
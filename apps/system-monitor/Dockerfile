FROM python:3.9-slim
WORKDIR /app
RUN pip install flask psutil
COPY app.py .
CMD ["python", "app.py"]
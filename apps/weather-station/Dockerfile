FROM python:3.9-slim
WORKDIR /app
RUN pip install flask requests psutil
COPY app.py .
CMD ["python", "app.py"]
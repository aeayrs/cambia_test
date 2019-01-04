FROM python:3-alpine
WORKDIR /workspace
COPY cambia.py ./
CMD ["python", "./cambia.py"]

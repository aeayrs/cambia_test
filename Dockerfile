FROM python:3
WORKDIR /workspace
COPY cambia.py ./
CMD ["python", "./cambia.py"]

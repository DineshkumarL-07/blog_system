FROM python:3.12.1-slim

WORKDIR /blog_system

COPY requirements.in .
RUN pip install --upgrade pip && pip install -r requirements.in

COPY . .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


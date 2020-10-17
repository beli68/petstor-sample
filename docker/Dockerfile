FROM python:3.8

COPY app/ /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /

EXPOSE 80
# FastAPIを8000ポートで待機
CMD ["hypercorn", "app.main:app" , "--bind", "0.0.0.0:80" , "--access-logfile", "-" , "--error-logfile", "-"]
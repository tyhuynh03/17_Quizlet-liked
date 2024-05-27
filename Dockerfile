# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Sao chép tệp requirements.txt vào thư mục làm việc trong container
COPY src/requirements.txt ./

# Cài đặt dependencies từ tệp requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn của dự án vào thư mục làm việc trong container
COPY src/ ./

# reset db
RUN python manage.py flush --no-input

# Thực hiện migrations
RUN python manage.py makemigrations && \
    python manage.py migrate

RUN echo "from users.models import User; User.objects.create_superuser('admin', 'admin@gmail.com', 'Admin@12345')" | python manage.py shell

# Sao chép các script Python vào thư mục làm việc trong container
COPY installation/scripts/ /app/scripts/

# Chạy các script để tạo dữ liệu mẫu
# Thực thi script import_data
RUN python manage.py runscript import_data
RUN python manage.py runscript populate_data_from_csv



# Command để chạy ứng dụng của bạn
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

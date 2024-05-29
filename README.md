# Ứng dụng tạo câu hỏi trắc nghiệm (Quizlet-liked)
Mô tả ứng dụng
# Tên ứng dụng: Quizlet
Quizlet là một ứng dụng học tập trực tuyến giúp người dùng tạo và tham gia các bài trắc nghiệm để kiểm tra kiến thức và kỹ năng của mình. Ứng dụng giải quyết vấn đề cải thiện hiệu quả học tập và đánh giá thông qua các bài kiểm tra ngắn gọn và trực quan.
# Đối tượng người dùng:
- Học sinh và sinh viên: Sử dụng để ôn tập và kiểm tra kiến thức các môn học.
- Giáo viên và giảng viên: Tạo và quản lý các bài kiểm tra cho học sinh.
- Người tự học: Tự kiểm tra và cải thiện kỹ năng và kiến thức cá nhân.
# Các chức năng chính:
- Đăng nhập và đăng ký: Cho phép người dùng tạo tài khoản và đăng nhập để sử dụng các tính năng của ứng dụng.
- Tạo và tham gia bài trắc nghiệm: Người dùng có thể tạo các bài trắc nghiệm mới hoặc tham gia các bài trắc nghiệm có sẵn.
- Quản lý câu hỏi và chủ đề: Hỗ trợ thêm câu hỏi và chủ đề mới, bao gồm đính kèm hình ảnh minh họa.
- Nhập câu hỏi từ file CSV: Tạo bài trắc nghiệm nhanh chóng bằng cách nhập câu hỏi từ file CSV.
- Hiển thị kết quả và phân tích: Cung cấp kết quả chi tiết và biểu đồ trực quan về câu trả lời đúng và sai.

- Bạn có thể trải nghiệm ứng dụng ở đây [LINK](https://one7-quizlet-liked.onrender.com/)
- Một số sceenshot của ứng dụng
![Alt text](./docs/images/home.png)
![Alt text](./docs/images/login.png)
![Alt text](./docs/images/quizlet.png)

## CÀI ĐẶT

Hướng dẫn cài đặt và chạy sau khi pull project từ github về (Lưu ý: hướng dẫn phải chạy được). Bao gồm:
- Các phần mềm cần cài đặt
- Các gói thư viện python cần dùng (có thể sử dụng pip freeze để tạo)
- Script tạo database (Để script trong thư mục installation)
- Script tạo dữ liệu (Để script trong thư mục installation)
# Hướng dẫn cài đặt và chạy bằng docker
- 1. Cài Đặt Docker: Đảm bảo rằng tất cả người dùng đã cài đặt Docker trên máy tính của họ. Bạn có thể hướng dẫn họ cài đặt Docker từ trang chính thức docker.com.
- 2. Pull Project từ GitHub: Đầu tiên, hãy sử dụng Git để pull project từ GitHub về máy tính của bạn. Bạn có thể sử dụng lệnh sau trong terminal hoặc command prompt:
      - git clone https://github.com/tyhuynh03/17_Quizlet-liked/
- 3. Chạy Docker Compose:
     - Điều hướng đến thư mục gốc của project đã clone.
     - Chạy lệnh sau để tạo và chạy Docker containers từ file docker-compose.yml:
     - docker-compose up --build
- Sau khi các containers được khởi động, ứng dụng web sẽ được chạy trên địa chỉ http://localhost:8000/.

# Hướng dẫn cài đặt và chạy bằng máy local
- Ngoài cách chạy bằng docker chúng ta có thể chaỵ trực tiếp trên máy local
- 1. Pull Project từ GitHub: Đầu tiên, hãy sử dụng Git để pull project từ GitHub về máy tính của bạn. Bạn có thể sử dụng lệnh sau trong terminal hoặc command prompt:
    git clone https://github.com/tyhuynh03/17_Quizlet-liked/
- 2. Copy thư mục scrips vào src
- 3. Mở terminal và chạy xcopy installation\scripts src\scripts /s /e /i
- 4. Điều hướng đến thư mục src: cd src
- 5. Chạy các câu lệnh trên terminal theo thứ tự:
     python manage.py makemigrations -> python manage.py migrate ->
     python manage.py createsuperuser -> 
     python manage.py runscript import_data ->
     python manage.py runscript populate_data_from_csv ->  
     -> python manage.py runserver
- Sau khi hoàn tất các bước, web sẽ được chạy trên địa chỉ http://127.0.0.1:8000/.

## THÔNG TIN THÀNH VIÊN

- Huỳnh Tấn Tỷ - 21093521
- Hoàng Thanh Tú - 21105251
- Nguyễn Khắc Luật - 21099741
- Phạm Nhựt Minh - 21021471

## TRÁCH NHIỆM

- Thành viên 1: Huỳnh Tấn Tỷ
    - Trách nhiệm 1: Phát triển backend và cơ sở dữ liệu
    - Trách nhiệm 2: Xây dựng và tích hợp frontend
    - Trách nhiệm 3: Quản lý source code trên git
    - Trách nhiệm 4: Quản lý và triển khai dự án trên máy chủ
- Thành viên 2: Hoàng Thanh Tú
    - Trách nhiệm 1: Thiết kế giao diện người dùng (UI/UX)
    - Trách nhiệm 2: Kiểm thử và đảm bảo chất lượng sản phẩm (QA)
    - Trách nhiệm 3: Quản lý bảo mật và xác thực người dùng
    - Trách nhiệm 4: Giám sát và xử lý các lỗi phát sinh trong quá trình sử dụng
- Thành viên 3: Nguyễn Khắc Luật
    - Trách nhiệm 1: Thiết kế giao diện người dùng (UI/UX)
    - Trách nhiệm 2: Tạo các mẫu giao diện cho các trang web chính
    - Trách nhiệm 3: Kiểm thử và đảm bảo chất lượng sản phẩm (QA)
    - Trách nhiệm 4: Giám sát và xử lý các lỗi phát sinh trong quá trình sử dung
- Thành viên 4: Phạm Nhựt Minh
    - Trách nhiệm 1: Phát triển backend và cơ sở dữ liệu
    - Trách nhiệm 2: Cập nhật và bảo trì hệ thống sau khi triển khai
    - Trách nhiệm 3: Đảm bảo hiệu suất và tối ưu hóa máy chủ
    - Trách nhiệm 4: Giám sát và xử lý các lỗi phát sinh trong quá trình sử dụng

---
+ Video demo project: https://youtu.be/M7Yl7N7EF1E
---

## 2. PHÂN TÍCH

### 2.1 Giới thiệu

#### 2.1.1. Mục đích

Mục đích của tài liệu này nhằm mô tả một cách đầy đủ và toàn diện yêu cầu của ứng dụng: các yêu cầu chức năng, yêu cầu phi chức năng, các ràng buộc về mặt thiết kế.

* Yêu Cầu Chức Năng (Functional Requirements):
  - Quản lý Người Dùng:
    + Chức năng đăng nhập và đăng ký.
    + Khả năng tạo, chỉnh sửa và xóa người dùng (chỉ dành cho admin).
    + Quản lý vai trò của người dùng (admin hoặc user).
  - Quản Lý Chủ Đề:
    + Tạo, chỉnh sửa và xóa chủ đề câu hỏi.
    + Liệt kê danh sách chủ đề câu hỏi.
  - Quản Lý Câu Hỏi:
    + Tạo, chỉnh sửa và xóa câu hỏi trong từng chủ đề.
    + Hiển thị danh sách câu hỏi trong mỗi chủ đề.
  - Trả Lời Câu Hỏi:
    + Người dùng có thể trả lời các câu hỏi có sẵn trong hệ thống.
    + Tính điểm và hiển thị kết quả sau khi trả lời câu hỏi.
* Yêu Cầu Phi Chức Năng (Non-functional Requirements):
  - Giao Diện Người Dùng:
    + Giao diện thân thiện, dễ sử dụng.
    + Tốc độ tải trang nhanh chóng.
  - Bảo Mật:
    + Hệ thống phải đảm bảo an toàn thông tin người dùng và dữ liệu câu hỏi.
* Ràng Buộc Thiết Kế (Design Constraints):
  - Công Nghệ:
    + Sử dụng Django framework cho backend và HTML, CSS, JavaScript cho frontend.
    + Sử dụng cơ sở dữ liệu quan hệ MySQL

#### 2.1.2 Phạm vi

Mô tả ngắn gọn đặc điểm của ứng dụng; phạm vi, đối tượng phục vụ của ứng dụng; nhóm các hệ thống con
Chỉ ra được tài liệu này dùng cho đối tượng nào?

- Phạm vi: Ứng dụng hướng đến người dùng muốn tự kiểm tra kiến thức hoặc tạo bài kiểm tra để chia sẻ với người khác.
- Đối Tượng Phục Vụ:
  + Sinh viên, học sinh muốn ôn tập kiến thức.
  + Giáo viên muốn tạo bài kiểm tra cho học sinh.
  + Các chuyên gia muốn chia sẻ kiến thức chuyên môn.


### 2.2 Phân tích yêu cầu

#### 2.2.1 Đặc tả Actors

- Actor 1: Admin
  * Mô tả: Người quản trị hệ thống, có quyền truy cập vào tất cả các chức năng và tính năng của trang web.

- Actor 2: User
  * Mô tả: Người dùng cuối, tham gia vào việc tạo, trả lời câu hỏi và sử dụng các tính năng khác của trang web.


#### 2.2.2 Đặc tả Use-cases

- Danh sách các use-cases:
    - UC01: đăng ký/đăng nhập
        + Nếu chưa có tài khoản thì sẽ vào giao diện đăng ký. Đăng ký thì cần gmail, tên đăng nhập và mật khẩu
        + Sau khi đăng nhập thì tùy vào loại tài khoản mà vào 2 giao diện khác nhau: giao diện cho admin và giao diện cho user
    - UC02: quản lý chủ đề, câu hỏi
        + Quản lý chủ đề: tạo, chỉnh sửa, xóa chủ đề câu hỏi.
        + Quản lý câu hỏi: tạo, chỉnh sửa, xóa câu hỏi.
        + Xem danh sách chủ đề, câu hỏi đã có
    - UC03: tìm kiếm
        + Tìm kiếm câu hỏi, chủ đề có sẵn
    - UC04: làm kiểm tra
        + Làm kiểm tra trên bộ câu hỏi đã chọn
        + Xem thống kê, tính điểm
    - UC05: Quản lý tài khoản 
        + Tạo, chỉnh sửa, xóa tài khoản
        + Xem, xóa, sửa thông tin cá nhân
    - UC06: Xem thống kê và báo cáo
        + Xem số chủ đề, câu hỏi đã tạo
        + Xem thời gian làm kiểm tra, tỷ lệ trả lời đúng
- Liệt kê các use-cases theo actor: (LƯU Ý: nếu phần này các chức năng thực hiện khác nhau ở mỗi actor thì ghi rõ các khác nhau đó)
    - Actor 1: Admin
        - UC01: đăng ký, đăng nhập
        - UC02: quản lý chủ đề, câu hỏi
            + tạo và chỉnh sửa, xóa chủ đề, câu hỏi của TẤT CẢ người dùng
        - UC03: tìm kiếm
        - UC04: làm kiểm tra
        - UC05: Quản lý tài khoản 
            + Tạo, chỉnh sửa, xóa tài khoản của TẤT CẢ người dùng
            + Xem, xóa, sửa thông tin cá nhân
        - UC06: Xem thống kê và báo cáo
            + Xem số chủ đề, câu hỏi đã tạo của TẤT CẢ người dùng
            + Xem thời gian làm kiểm tra, tỷ lệ trả lời đúng của TẤT CẢ người dùng
    - Actor 2: User
        - UC01: đăng ký, đăng nhập
        - UC02: quản lý chủ đề, câu hỏi
            + tạo và chỉnh sửa, xóa chủ đề, câu hỏi của CÁ NHÂN
            + chỉ có quyền xem chủ đề và câu hỏi của người khác
        - UC03: tìm kiếm
        - UC04: làm kiểm tra
        - UC05: Quản lý tài khoản 
            + Tạo, chỉnh sửa, xóa tài khoản của CÁ NHÂN
            + Xem, xóa, sửa thông tin cá nhân
        - UC06: Xem thống kê và báo cáo
            + Xem số chủ đề, câu hỏi đã tạo của CÁ NHÂN
            + Xem thời gian làm kiểm tra, tỷ lệ trả lời đúng của CÁ NHÂN

1. Đặc điểm
- Kiểu dữ liệu TUPLE chứa tập hợp danh sách không thể thay đổi (immutable)
=> sau khi khởi tạo, giá trị của nó không thể thay đổi (bất biến - không thể thêm, xóa, sửa,...)

*VD:
    my_tuple = (1, 2, 3)
    my_tuple[0] = 10    => Lỗi 

- Có thể chứa các phần tử trùng nhau
- Hỗ trợ nhiều kiểu dữ liệu (số, chuỗi, danh sách,...)

2. Cách khai báo
- Dùng ngoặc tròn "()" để tạo 1 tuple, dấu "," để phân tách các phần tử
- Có thể bỏ ngoặc tròn để viết tắt (không khuyến khích)

*VD:
    my_tuple = (1, 2, 3)
    my_tuple = 1, 2, "ba"

- Có thể khai báo 1 tuple rỗng
- Trong trường hợp khai báo tuple chỉ có 1 phần tử, cần thêm dấu "," để hiểu là đang khởi tạo 1 tuple

*VD:
    my_tuple = (1 ,)

- Có thể chuyển tuple -> list và ngược lại

*VD:
    list(my_tuple) và tuple(my_list)

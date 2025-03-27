# CÁC PHƯƠNG THỨC LÀM VIỆC VỚI LIST (DANH SÁCH)

danh_sach = [1, 2, 3]

# 1. APPEND 
# - dùng để thêm 1 phần tử vào cuối danh sách

danh_sach.append(4)

# kq => [1, 2, 3, 4]
# i  => [0, 1, 2, 3]


# 2. EXTEND
# - dùng để mở rộng danh sách bằng cách thêm tất cả các phần tử từ 1 iterible(list, tuple, set,...)
#   vào cuối danh sách

danh_sach.extend([4, 5])

# kq => [1, 2, 3, 4, 4, 5]
# i  => [0, 1, 2, 3, 4, 5]

# 3. INSERT 
# - dùng để chèn phần tử (value) vào vị trí (index) mong muốn
# - phương thức INSERT đối số thứ nhất truyền vào là vị trí mong muốn, đối số thứ hai là giá trị muốn chèn
# - vd: chèn phần tử 0 vào vị trí index 0 (đầu tiên)

danh_sach.insert(0, 0)

# kq => [0, 1, 2, 3, 4, 4, 5]
# i  => [0, 1, 2, 3, 4, 5, 6]


# 4. REMOVE
# - dùng để xóa phần tử đầu tiên có giá trị = với đối số truyền vào
# - nếu không tìm thấy phần tử trùng khớp => báo lỗi ValueError

danh_sach.remove(4)

# kq => [0, 1, 2, 3, 4, 5]
# i  => [0, 1, 2, 3, 4, 5]


# 5. POP
# - dùng để loại bỏ và trả về phần tử
# - có hoặc không yêu cầu cần giá trị truyền vào
# nếu không có giá trị truyền vào, mặc định giá trị sẽ là -1 (phần tử cuối) 
# - vd: xóa phần tử cuối cùng

danh_sach.pop()

# kq => [0, 1, 2, 3, 4]
# i  => [0, 1, 2, 3, 4]

# - vd: xóa phần tử tại vị trí cụ thể

danh_sach.pop(0)

# kq => [1, 2, 3, 4, 5]
# i  => [0, 1, 2, 3, 4]


# SỰ KHÁC NHAU GIỮA REMOVE VÀ POP
# - POP: xóa phần tử theo vị trí
# 
# - REMOVE: xóa phần tử theo giá trị (giá trị khớp đầu tiên)     


# 6. CLEAR
# - xóa toàn bộ các phần tử trong danh sách, để lại danh sách rỗng

danh_sach.clear()

# kq => []


danh_sach_2 = [1, 2, 3, 4, 4, 5, 6]

# 7. INDEX(value, start end,)
# - dùng để trả về chỉ số (index) đầu tiên của giá trị truyền vào (bắt buộc)
# - có thể giới hạn phạm vi tìm kiếm bằng START và END (tùy chọn)

# - vd:

# ds => [1, 2, 3, 4, 4, 5]
# i  => [0, 1, 2, 3, 4, 5]

i = danh_sach_2.index(4, 4)

# print(i)

# start sẽ bắt đầu từ index = 4 (bỏ qua số 4 đầu tiên vì có index = 3), và tìm thấy phần tử 4 có vị trí index = 4
# kq => i = 4


# 8. COUNT
# - dùng để đếm số lần xuất hiện của phần tử có trong danh sách dựa theo đối số truyền vào

# print(danh_sach_2.count(4))

# kq = 2 (phần tử 4 xuất hiện 2 lần trong danh sách) 


# 9. SORT
# .sort(key=NONE, reverse=False)
# - dùng để sắp xếp danh sách theo thứ tự tăng dần (mặc định)
# - reverse=True => thứ tự giảm dần
# - key: là hàm tùy chỉnh để xác định cách sắp xếp

list_messed = [3, 2, 6, 1, 5, 4]

# sắp xếp tăng dần (mặc định)
list_messed.sort()
# kq => [1, 2, 3, 4, 5, 6]

# sắp xếp giảm dần
list_messed.sort(reverse=True)
# kq => [6, 5, 4, 3, 2, 1]
# print(list_messed)

# sắp xếp theo key
# các key cơ bản:
# len : độ dài chuỗi
# abs : theo giá trị tuyệt đối (không quan tâm dấu âm)
# str.lower : sắp xếp theo chữ cái đầu viết hoa


# 10. REVERSE
# - dùng để đảo ngược thứ tự phần từ trong danh sách

danh_sach_2.reverse()

# kq => [6, 5, 4, 3, 2, 1]


# 11. COPY
# - dùng để tạo 1 bản sao (shallow copy) của danh sách

copy = danh_sach_2.copy()

print(copy)
# ===========================================================================


# ============================== LƯU Ý ======================================

# - các phương thức: APPEND, REMOVE, SORT,... sẽ thay đổi trực tiếp danh sách
#   gốc (in-place), không tạo ra danh sách mới

# - 1 số phương thức: POP, INDEX - trả về giá trị, trong khi các phương thức
#   khác: APPEND, CLEAR - không trả về gì cả(NONE)

# ===========================================================================
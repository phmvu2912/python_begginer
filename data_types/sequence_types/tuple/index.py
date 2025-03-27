# KHAI BÁO TUPLE

my_tuple = [1, "hai", 3.14, ["apple", "banana"], 3.14]

# CÁC THAO TÁC CƠ BẢN VỚI TUPLE

# 1. COUNT
# - Đếm số lần lặp lại của phần tử trong tập hợp

# print(my_tuple.count(1))


#  2. LEN
# - Đếm số lượng phần tử trong tập hợp

# print(len(my_tuple))


# 3. SLICING 
# - Trích xuất 1 phần của tập hợp bằng cách chỉ định phạm vi thông qua chỉ mục (index)
# my_tuple[start:stop:step]
# - start: index bắt đầu
# - stop: index kết thúc
# - step: bước nhảy giữa các phần tử (mặc định là 1 nếu bỏ trống)

my_tuple_2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# print(my_tuple_2[1:5:2])  # => kq = 2, 4

# - nếu muốn lấy 1 tập hợp từ phần tử đến cuối => my_tuple_2[x:]
# - nếu muốn lấy toàn bộ tuple => my_tuple_2[:]
# - nếu muốn đảo ngược thứ tự các phần tử => my_tuple_2[::-1]
# - có thể dùng chỉ số âm để cắt từ cuối tập hợp => my_tuple_2[-3:] => kq = 7, 8, 9
# - nếu start > stop => tuple rỗng


# 4. NỐI TUPLE 
# - Dùng toán tử (+) để nối các tuple lại tạo thành 1 tuple mới chứa các phần tử của tuple đó

t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2

# print(t3) # => kq = 1, 2, 3, 4


# 5. NHÂN BẢN TUPLE
# - Dùng toán tử * để nhân bản các phần tử

t4 = (5, 6, 7)

new_t = t4 * 2

# print(new_t) # => kq = 5, 6, 7, 5, 6, 7


# 6. IN
# - Dùng toán tử in để kiểm tra phần tử có trong 1 tuple không và trả về True hoặc False
# print("ba" in my_tuple) # => kq = False


# 7. Tìm chỉ mục (index)
# - Dùng phương thức index() để tìm chỉ số đầu tiên của 1 giá trị trong tuple

# print(my_tuple.index(3.14)) # => kq = 3.14 đầu tiên có index = 2


# 8. Giải nén tuple
# - Gán các phần tử của tuple vào các biến riêng lẻ
tuple_8 = (10, 20, 30)

a, b, c = tuple_8

print(a)
print(b)
print(c)

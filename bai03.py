# Input:
#  raw_data: chuỗi dữ liệu nhân sự (string)
#  lựa chọn menu từ người dùng
#  mã nhân viên cần tìm

# Output:
#  Hiển thị dữ liệu gốc
#  Báo cáo nhân sự đã chuẩn hóa
#  Tìm kiếm nhân viên theo ID
#  Thoát chương trình

# Giải pháp:
# 1. Dùng split("|") để tách từng nhân viên
# 2. Dùng split(";") để tách từng trường thông tin
# 3. Chuẩn hóa dữ liệu:
#     ID: upper()
#     Họ tên: title()
#     Phòng ban: upper()
#     SĐT:
#         xóa dấu "-"
#         nếu chỉ chứa số -> che 6 số đầu
#         nếu có ký tự chữ -> Invalid Format
# 4. Tìm kiếm:
#     strip() + upper() dữ liệu nhập
#     so sánh với ID đã chuẩn hóa
# 5. Kiểm tra nhập sai menu:
#     nếu nhập ngoài 1-4 hoặc nhập chữ
#      -> báo lỗi và hiển thị lại menu


raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "


# Hàm xử lý số điện thoại
def format_phone(phone):
    # Xóa khoảng trắng và dấu -
    phone = phone.strip().replace("-", "")

    # Kiểm tra hợp lệ
    if phone.isdigit():
        return "******" + phone[-4:]

    return "Invalid Format"

def normalize_employee(employee):
    parts = employee.split(";")

    employee_id = parts[0].strip().upper()
    full_name = parts[1].strip().title()
    phone = format_phone(parts[2])
    department = parts[3].strip().upper()

    return employee_id, full_name, phone, department

# MENU HỆ THỐNG
while True:
    print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    # Kiểm tra nhập menu hợp lệ
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    choice = int(choice)

    # CHỨC NĂNG 1: HIỂN THỊ DỮ LIỆU GỐC
    if choice == 1:
        print("\n===== DỮ LIỆU GỐC =====")
        print(raw_data)

    # CHỨC NĂNG 2: CHUẨN HÓA DỮ LIỆU
    elif choice == 2:
        print("\n===== BÁO CÁO NHÂN SỰ =====")

        print(f"{'ID':<12}{'HỌ TÊN':<25}{'SỐ ĐIỆN THOẠI':<20}{'PHÒNG BAN'}")
        print("-" * 70)

        employees = raw_data.split("|")

        for employee in employees:
            employee_id, full_name, phone, department = normalize_employee(employee)

            print(
                f"{employee_id:<12}"
                f"{full_name:<25}"
                f"{phone:<20}"
                f"{department}"
            )

    # CHỨC NĂNG 3: TÌM KIẾM NHÂN VIÊN
    elif choice == 3:
        search_id = input("Nhập mã nhân viên cần tìm: ").strip().upper()

        found = False

        employees = raw_data.split("|")

        for employee in employees:
            employee_id, full_name, phone, department = normalize_employee(employee)

            if employee_id == search_id:
                print("\n===== THÔNG TIN NHÂN VIÊN =====")
                print("ID:", employee_id)
                print("Họ tên:", full_name)
                print("SĐT:", phone)
                print("Phòng ban:", department)

                found = True
                break

        if not found:
            print("Không tìm thấy nhân viên")
    # CHỨC NĂNG 4: THOÁT
    elif choice == 4:
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
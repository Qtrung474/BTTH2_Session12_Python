# 1. Phân tích Input/Output
# Input (Dữ liệu đầu vào):
# Lựa chọn menu: Số nguyên int (từ 1 đến 7).
# Mã sổ tiết kiệm: Chuỗi ký tự string.
# Tên khách hàng: Chuỗi ký tự string.
# Số tiền gửi, kỳ hạn gửi, số tháng thực gửi: Số nguyên dương int.
# Lãi suất năm: Số thực dương float.
# Output (Dữ liệu đầu ra):
# Danh sách sổ tiết kiệm hiện có trong hệ thống.
# Các thông báo trạng thái thao tác (Thành công/Thất bại).
# Kết quả tính toán lãi suất (Tiền lãi, Tổng tiền nhận).
# Các thông báo lỗi khi vấp phải Edge Cases (nhập sai kiểu dữ liệu, bỏ trống, âm...).
# 2. Đề xuất giải pháp
# Lưu trữ dữ liệu: Quản lý bằng một danh sách chứa các dictionary (saving_accounts).
# Xử lý chuỗi: Sử dụng phương thức .strip() để loại bỏ khoảng trắng thừa và .upper() để chuẩn hóa mã sổ tiết kiệm.
# Kiểm tra tính hợp lệ (Validation): Dùng khối lệnh try...except ValueError để bắt lỗi nhập sai kiểu dữ liệu 
# (chữ cái thay vì số) cho tiền gửi, kỳ hạn, lãi suất. Kếp hợp vòng lặp điều kiện if...else để kiểm tra các giá trị âm hoặc bằng 0.
# Tìm kiếm: Tạo một hàm hỗ trợ để duyệt qua danh sách và trả về dictionary của sổ tiết kiệm nếu mã sổ khớp, 
# giúp tái sử dụng code cho các chức năng cập nhật, tất toán và tính lãi.
# 3. Thiết kế thuật toán (Luồng chương trình)
# Khởi tạo danh sách saving_accounts với dữ liệu ban đầu.
# Hiển thị Menu vô hạn bằng vòng lặp while True.
# Nhận đầu vào từ người dùng cho lựa chọn menu.
# Nếu chọn 1: Duyệt và in danh sách. Nếu rỗng thì báo trống.
# Nếu chọn 2: Nhập thông tin, kiểm tra mã trùng, kiểm tra rỗng, ép kiểu int/float và kiểm tra > 0. 
# Thêm vào danh sách với trạng thái "active".
# Nếu chọn 3: Nhập mã, tìm kiếm. Nếu không thấy hoặc trạng thái "closed", báo lỗi. Nếu hợp lệ,
# cho phép nhập dữ liệu mới (kèm validation) và ghi đè dữ liệu cũ.
# Nếu chọn 4: Nhập mã, tìm kiếm. Nếu hợp lệ, đổi trạng thái thành "closed".
# Nếu chọn 5: Nhập mã, tìm kiếm. Kiểm tra trạng thái "active". Áp dụng công thức tính lãi đến hạn.
# Nếu chọn 6: Nhập mã, tìm kiếm. Kiểm tra trạng thái "active". Nhập và kiểm tra số tháng thực gửi. 
# So sánh với kỳ hạn để quyết định mức lãi suất (0.5% hoặc lãi gốc) và tính tiền.
# Nếu chọn 7: break khỏi vòng lặp để thoát chương trình.
# Mặc định (Edge Case 8): In thông báo nhập sai menu.

saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")
    
    choice = input("Mời bạn chọn chức năng (1-7): ")
    
    if choice == "1":
        if len(saving_accounts) == 0:
            print("Danh sách sổ tiết kiệm hiện đang trống")
        else:
            print("Danh sách sổ tiết kiệm:")
            count = 1
            for acc in saving_accounts:
                print(f"{count}. Mã sổ: {acc['account_id']} | Khách hàng: {acc['customer_name']} | Số tiền gửi: {acc['balance']} | Kỳ hạn: {acc['term_months']} tháng | Lãi suất: {acc['interest_rate']}%/năm | Trạng thái: {acc['status']}")
                count += 1
                
    elif choice == "2":
        account_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()
        
        is_exist = False
        for acc in saving_accounts:
            if acc["account_id"] == account_id:
                is_exist = True
                break
                
        if is_exist:
            print("Mã sổ tiết kiệm đã tồn tại!")
        else:
            customer_name = input("Nhập tên khách hàng: ").strip()
            if customer_name == "":
                print("Tên khách hàng không được để trống")
            else:
                balance_str = input("Nhập số tiền gửi: ")
                term_str = input("Nhập kỳ hạn gửi theo tháng: ")
                rate_str = input("Nhập lãi suất năm: ")
                
                if not balance_str.isdigit() or not term_str.isdigit():
                    print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                else:
                    balance = int(balance_str)
                    term_months = int(term_str)
                    
                    try:
                        interest_rate = float(rate_str)
                        if balance <= 0 or term_months <= 0:
                            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                        elif interest_rate <= 0:
                            print("Lãi suất không hợp lệ!")
                        else:
                            new_account = {
                                "account_id": account_id,
                                "customer_name": customer_name,
                                "balance": balance,
                                "term_months": term_months,
                                "interest_rate": interest_rate,
                                "status": "active"
                            }
                            saving_accounts.append(new_account)
                            print("Mở sổ tiết kiệm thành công!")
                    except ValueError:
                        print("Lãi suất không hợp lệ!")

    elif choice == "3":
        account_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()
        
        found_account = None
        for acc in saving_accounts:
            if acc["account_id"] == account_id:
                found_account = acc
                break
                
        if found_account == None:
            print("Không tìm thấy mã sổ tiết kiệm")
        elif found_account["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán")
        else:
            customer_name = input("Nhập tên khách hàng mới: ").strip()
            if customer_name == "":
                print("Tên khách hàng không được để trống")
            else:
                balance_str = input("Nhập số tiền gửi mới: ")
                term_str = input("Nhập kỳ hạn mới theo tháng: ")
                rate_str = input("Nhập lãi suất năm mới: ")
                
                if not balance_str.isdigit() or not term_str.isdigit():
                    print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                else:
                    balance = int(balance_str)
                    term_months = int(term_str)
                    
                    try:
                        interest_rate = float(rate_str)
                        if balance <= 0 or term_months <= 0:
                            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                        elif interest_rate <= 0:
                            print("Lãi suất không hợp lệ!")
                        else:
                            found_account["customer_name"] = customer_name
                            found_account["balance"] = balance
                            found_account["term_months"] = term_months
                            found_account["interest_rate"] = interest_rate
                            print("Cập nhật thông tin sổ tiết kiệm thành công!")
                    except ValueError:
                        print("Lãi suất không hợp lệ!")

    elif choice == "4":
        account_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()
        
        found_account = None
        for acc in saving_accounts:
            if acc["account_id"] == account_id:
                found_account = acc
                break
                
        if found_account == None:
            print("Không tìm thấy mã sổ tiết kiệm")
        elif found_account["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán")
        else:
            found_account["status"] = "closed"
            print("Tất toán sổ tiết kiệm thành công!")

    elif choice == "5":
        account_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()
        
        found_account = None
        for acc in saving_accounts:
            if acc["account_id"] == account_id:
                found_account = acc
                break
                
        if found_account == None:
            print("Không tìm thấy mã sổ tiết kiệm")
        elif found_account["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán")
        else:
            interest = found_account["balance"] * found_account["interest_rate"] / 100 * found_account["term_months"] / 12
            total = found_account["balance"] + interest
            
            print(f"Tiền lãi dự kiến: {interest:.2f}")
            print(f"Tổng tiền nhận khi đến hạn: {total:.2f}")

    elif choice == "6":
        account_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()
        
        found_account = None
        for acc in saving_accounts:
            if acc["account_id"] == account_id:
                found_account = acc
                break
                
        if found_account == None:
            print("Không tìm thấy mã sổ tiết kiệm")
        elif found_account["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán")
        else:
            actual_months_str = input("Nhập số tháng thực gửi: ")
            
            if not actual_months_str.isdigit():
                print("Số tháng thực gửi không hợp lệ!")
            else:
                actual_months = int(actual_months_str)
                if actual_months <= 0:
                    print("Số tháng thực gửi không hợp lệ!")
                else:
                    if actual_months < found_account["term_months"]:
                        applied_rate = 0.5
                    else:
                        applied_rate = found_account["interest_rate"]
                        
                    interest = found_account["balance"] * applied_rate / 100 * actual_months / 12
                    total = found_account["balance"] + interest
                    
                    print(f"Lãi suất áp dụng: {applied_rate}%/năm")
                    print(f"Tiền lãi thực nhận: {interest:.2f}")
                    print(f"Tổng tiền thực nhận: {total:.2f}")

    elif choice == "7":
        print("Đã thoát chương trình.")
        break
        
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")
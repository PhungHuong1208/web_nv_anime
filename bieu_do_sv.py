so_nam = int(input("Nhập số sinh viên nam: "))
so_nu = int(input("Nhập số sinh viên nữ: "))
max_height = max(so_nam, so_nu)
print("\n=== BIỂU ĐỒ CỘT  ===")
for row in range(max_height, 0, -1):
    col_nam = "  █  " if so_nam >= row else "     "
    col_nu  = "  █  " if so_nu >= row else "     "
    print(f"{col_nam}  {col_nu}")
print("-----  -----")
print(f" ({so_nam:2d})    ({so_nu:2d})")
print(" Nam     Nữ ")


emp_number, hours, rate = [convert(input()) for convert in (int, int, float)]
print(f"NUMBER = {emp_number}\nSALARY = U$ {hours * rate:.2f}")
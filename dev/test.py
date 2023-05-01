from shift_register import ShiftRegister

sr = ShiftRegister(11, 13, 15, 10)

data_list = []
for _ in range(10):
    data_list.extend([0, 1, 1, 0, 0, 0, 0, 1])

sr.shift_out(data_list)

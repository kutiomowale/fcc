# Counting on one hand in binary
def count_one_hand(i):
    if type(i) is not int:
        return []
    if i < 0 or i > 31:
        return []
    bin_i = bin(i)[2:].zfill(5)
    legend = ['Pinky', 'Ring', 'Middle', 'Index', 'Thumb']
    result = []
    for bit, finger in zip(bin_i, legend):
        if bit == '1':
            result.append(finger)
    return result

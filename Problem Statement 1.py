def countNumbers(num):
    count = 0
    for i in range(10**(num-1), 10**num):
        digits = [int(d) for d in str(i)]
        if all(digits[j] < digits[j+1] for j in range(len(digits)-1)):
            count += 1
    return count
num= eval(input("Enter the digit: "))
count = countNumbers(num)
print("Number of valid {}-digit numbers: {}".format(num, count))
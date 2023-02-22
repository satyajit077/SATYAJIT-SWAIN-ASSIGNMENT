import json
def generate_addition_steps(num1, num2):
    num1_str = str(num1)[::-1]
    num2_str = str(num2)[::-1]
    carry = 0
    carry_str = ""
    steps = {}
    for i in range(max(len(num1_str), len(num2_str))):
        digit1 = int(num1_str[i]) if i < len(num1_str) else 0
        digit2 = int(num2_str[i]) if i < len(num2_str) else 0
        total = digit1 + digit2 + carry
        if total >= 10:
            carry = 1
            total -= 10
        else:
            carry = 0
        carry_str += str(carry)
        total_str = str(total).zfill(len(num1_str))
        step = {"carryString": carry_str[::-1], "sumString": total_str[::-1]}
        steps["step{}".format(i+1)] = step
    return json.dumps(steps, indent=4)

num1 = 1489
num2 = 714
steps = generate_addition_steps(num1, num2)
print(steps)

def gen_seq(length):
    if (length <= 1):
        return length
    
    else:
        return gen_seq(length - 1) + gen_seq(length - 2)


length = int(input("input your sequence length:"))

print("The result is(using Recursion):")
for iter in range(length):
    print(gen_seq(iter))
def sum(a, b):
    return a + b

def safe_sum(a, b):
    if type(a) != type(b):
        print("더할 수 있는 값이 아님")
        return
    else:
        result = a + b
    return result

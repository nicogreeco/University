import textwrap

def wrap(string, max_width):
    a = (int(len(string)/max_width))
    for i in range(1,a+1):
        f = (i * (max_width)) + (i-1)
        string = string[:f] + "\n" + string[f:]
    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
w = 10
h = 15


def area(w, h):
    return w * h


area(w, h)

'''
    Multi
    line
    comment
'''

# lambda expression
sum = lambda arg1, arg2: arg1 + arg2
print('Value of total', sum(60, 40))


def print_info(name, salary=3500):
    """Print name and salary"""
    print('Name:', name)
    print('Salary:', salary)
    return


print_info('Joe', 4500)
print_info('Joe')


def printinfo(arg1, *vartuple):
    """this prints a variable passed arguments"""
    print('This is the output:')
    print(arg1)

    for var in vartuple:
        print(var)

    return


printinfo(100)
printinfo(20, 30, 40)

low_price = 4.99
high_price = 6.99


def low(lowprice, ):
    print('Chef salad with low-fat dressing')
    return lowprice


def high(highprice, ):
    print('Cheeseburger with French Fries')
    return highprice


meal = float(input('Enter 1 for a low calorie meal or 2 for a high calorie meal'))

if meal == 1:
    print(low(low_price))
else:
    print(high(high_price))

print("数据结构与算法6")
def sub_dict():
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    # Make a dictionary of all prices over 200
    p1 = {key: value for key, value in prices.items() if value > 200}
    # Make a dictionary of tech stocks
    tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    p2 = {key: value for key, value in prices.items() if key in tech_names}

if __name__ == '__main__':
    sub_dict()
from collections import namedtuple


def name_seq():
    subscriber = namedtuple('Subscriber', ['addr', 'joined'])
    sub = subscriber('jonesy@example.com', '2012-10-19')
    print(sub)
    print(sub.addr, sub.joined)

    print(len(sub))
    addr, joined = sub
    print(addr, joined)


def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


def compute_cost2(records):
    Stock = namedtuple('SSS', ['name', 'shares', 'price'])
    total = 0.0
    for rec in records:
        st = Stock(*rec)
        total += st.shares * st.price
    s = Stock('ACME', 100, 123.45)
    # 更新命名元组
    s = s._replace(shares=75)
    print(s)
    return total

Stock1 = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock1('', 0, 0.0, None, None)

# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

def default_stock():
    a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
    print(dict_to_stock(a))
    b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
    print(dict_to_stock(b))

if __name__ == '__main__':
    name_seq()
    # rs = [('aa', 12, 33)]
    rs = [['aa', 12, 33]]  # 元组和序列都可以
    print(compute_cost2(rs))
    default_stock()

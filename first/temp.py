def hello(greet='git'):
    return f'Hello, {greet}'


def changes():
    return f'This changes for second commit'


if __name__ == '__main__':
    print(hello('main'))
    print(changes())
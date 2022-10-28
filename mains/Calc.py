def calc(exp):
    allow = '+-/*'
    if not any(sign in exp for sign in allow):
        raise ValueError(f'Выражение должно содержать хотя бы один знак ({allow})')
    for sign in allow:
        if sign in exp:
            try:
                left, right = exp.split(sign)
                left, right = int(left), int(right)
                if sign == '+':
                    return left + right
                elif sign == '-':
                    return left - right
                elif sign == '*':
                    return left * right
                elif sign == '/':
                    return left / right
            except (ValueError,TypeError):
                raise ValueError('Выражение должно содержать 2 целых числа и 1 знак')


if __name__ == '__main__':
    print(calc('2/10'))

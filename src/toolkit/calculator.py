from .errors import (Invalid_Symbol_Error,
                     Invalid_Expression_Error,
                     Division_By_Zero_Error)

#разбиваем выражение на строки
def tokenization(expression: str) -> list[str]:
    tokens = []
    i = 0

    while i < len(expression):
        character = expression[i]

        if character == " ":
            i += 1
            continue

        if character in "+-*/":
            tokens.append(character)
            i += 1
            continue

        if character in "0123456789.":
            start = i
            while i < len(expression) and expression[i] in "0123456789.":
                i += 1

            tokens.append(expression[start:i])
            continue


        raise Invalid_Symbol_Error("Недопустимый символ")

    return tokens

#проверка токенов
def validation(tokens: list[str]) -> None:
    if not tokens:
        raise Invalid_Expression_Error("Выражение пустое")

    if tokens[0] in '*/':
        raise Invalid_Expression_Error("Первым ожидалось число")

    for i in range(len(tokens) -1):
        if tokens[i].isdigit() and tokens[i+1].isdigit():
            raise Invalid_Expression_Error("Ожидалась операция")

        if tokens[i] in '+-*/' and tokens[i+1] in '*/':
            raise Invalid_Expression_Error("Ожидалось число")

    if tokens[-1] in '+-*/':
        raise Invalid_Expression_Error("В конце ожидалось число")


#print(unar(['2','*','-','3']))

#унарность +-
def unar(token: list[str]) -> list[str]:
    i = 0
    while i < len(token):
        if token[i] in "+-":
            if (i == 0 or token[i-1] in "+-*/") and token[i+1] in "0123456789":
                token[i: i + 2] = [token[i] + token[i + 1]]
        i += 1
    return token

#юзлес
# def find_priority_operations(calculation: list[str]):
#     i = 0
#     while i < len(calculation):
#         if i%2 != 0:
#             if calculation[i] == '*':
#                 result = float(calculation[i-1]) * float(calculation[i+1])
#                 calculation = calculation[:i-1] + [str(result)] + calculation[i+2:]
#                 i = 0
#                 continue
#             elif calculation[i] == '/':
#                 result = float(calculation[i-1]) / float(calculation[i+1])
#                 calculation = calculation[:i-1] + [str(result)] + calculation[i+2:]
#                 i = 0
#                 continue
#         i = i + 1
#     return calculation


#переводит выражение в польскую нотацию
def RPN(tokens: list[str]) -> list[str]:
    output = []
    operators = []

    pr = {
        "+" : 1,
        "-" : 1,
        "*" : 2,
        "/" : 2,
    }

    for token in tokens:
        if token not in pr.keys():
            output.append(token)
        else:
            while len(operators) != 0 and pr[operators[-1]] >= pr[token]:
                tmp = operators.pop()
                output.append(tmp)
            operators.append(token)

    while len(operators) != 0 :
        tmp = operators.pop()
        output.append(tmp)
    return output


def solve_RPN(k: list[str]) -> float:
    st = []
    for i in k:
        if i in "*":
            first = float(st.pop())
            second =float(st.pop())
            z = first * second
            st.append(z)
        elif i in "/":
            first = float(st.pop())
            second = float(st.pop())
            if first == 0:
                raise Division_By_Zero_Error()
            z = second / first
            st.append(z)
        elif i in "+":
            first = float(st.pop())
            second = float(st.pop())
            z = first + second
            st.append(z)
        elif i in "-":
            first = float(st.pop())
            second = float(st.pop())
            z = second - first
            st.append(z)

        else:
            st.append(float(i))

    return st[0]

#соединяем все функции, разделяет, проверяет, вычисляет
def solve(token: str) -> float:
    z = unar(tokenization(token))
    validation(z)
    z = RPN(z)
    return solve_RPN(z)

##Скобочная последовательность [((())()(())]] не является правильной, т.к. в данной
##последовательности не для каждой закрывающей скобки есть соответствующая открывающая.
##Алгоритм для проверки скобочной последовательности может быть следующим:

string = input()
bracket_stack = []
is_right = True

for i in string:
    if i in "({[":
        bracket_stack.append(i)
    elif i in ")}]":
        if not bracket_stack:
            is_right = False
            break
        open_bkt = bracket_stack.pop()
        if open_bkt == "(" and i == ")":
            continue
        if open_bkt == "{" and i == "}":
            continue
        if open_bkt == "[" and i == "]":
            continue
        is_right = False
        break
if is_right and len(bracket_stack) == 0:
    print(f"Скобочная последовательность {string} верная")
else:
    print(f"Скобочная последовательность {string} не является верной")

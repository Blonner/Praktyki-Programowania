user_input = input("Podaj obiekt:")

if user_input.isdigit() or (user_input.startswith("-") and user_input[1:].isdigit()):
    data = int(user_input)
elif user_input.replace(".", "", 1).isdigit():
    data = float(user_input)
elif user_input.lower() == "true":
    data = True
elif user_input.lower() == "false":
    data = False
else:
    data = user_input


def handlerInt(obj):
    if isinstance(obj, int):
        print(f"Przetworzono liczbę całkowitą {obj}")
    else:
        handlerDouble(obj)


def handlerDouble(obj):
    if isinstance(obj, float):
        print(f"Przetworzono liczbę zmiennoprzecinkową {obj}")
    else:
        handlerBool(obj)


def handlerBool(obj):
    if isinstance(obj, bool):
        print(f"Przetworzono wartość logiczną {obj}")
    else:
        handlerString(obj)


def handlerString(obj):
    if isinstance(obj, str):
        print(f"Przetworzono tekst '{obj}'")
    else:
        print("Nieznany typ")


handlerInt(data)

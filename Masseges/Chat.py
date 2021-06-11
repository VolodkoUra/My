from MyUser import User
name = input("Введите имя пользователя чата: ")
#user = User(name, "http://127.0.0.1:50550/")
user = User(name, "http://johnray.pythonanywhere.com/")

#"http://127.0.0.1:50550/"
#"http://johnray.pythonanywhere.com/"

while True:
    print("Программа чат! Выберите действие, которое хотите выполнить: ")
    print("="*50)
    menu = input("1. Войти в чат.   2. Выйти из пограммы! ")
    if menu == "1":
        print("Вы вошли в чат!")
        print("-"*50)
        user.post_login()
        print("Программа чат! Для выхода нажмите 0!!! ")
        while True:
            print("-"*50)
            mes = input("Введите сообщение: ")
            user.send_massege(mes)
            user.get_massege()
            if mes == "0":
                print("Вы вышли из чата!")
                break

    elif menu == "2":
        break
    else:
        print("Введены не коректные данные! Попробуйте снова!")







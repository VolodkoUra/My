import time




exit()
def my_dec(f):


    def inner():
        start_time = time.time()
        res = f()
        end_time = time.time()
        print((end_time - start_time))
        return res
    return inner


@my_dec
def foo():
    r = 1
    for i in range(1000):
        r += i
    return r


print(foo())


exit()
import my_chat
import user

user1 = user.User("Alex")
user1.send_message("afafafa")
user1.send_message("afafafa")
user1.send_message("afafafa")
user1.send_message("afafafa")
user1.send_message("afafafa")

r = user1.get_massage_list()
print(r)

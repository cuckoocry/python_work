from zipimport import MAX_COMMENT_LEN

from Python编程从入门到实践.hello_world import message

name="ada lovelace"

print(name.title())

print(name.upper())

print(name.lower())


#########


first_name = "ada"
last_name = "lovelace"
# f字符串。f是format（设置格式）的简写
full_name = f"{first_name} {last_name}"

print(full_name)

message = f"Hello,{full_name.title()}!"

print(message)


print("Language:\n\tJava\n\tc\n\tpython\n")

###########s 删除空白

favorite_language = ' python '

print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

######## 删除前缀

nostarch_url = 'https://nostarch.com'

print(nostarch_url.removeprefix('https://'))


######  练习

name = '将大帅'

message = f"你好，{name},你吃饭了吗？"
print(message)

nameEnglish = 'jiang'
print(nameEnglish.upper())
print(nameEnglish.lower())
print(nameEnglish.title())


print('Albert Einstein once said, “A person who never made a mistake never tried anything new.”')

filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))





#######  2.4 数字

print(0.2+0.1)
# 将任意两个数相除，结果总是浮点数，即便这两个数都是整数且能整除：
# 无论是哪种运算，只要有操作数是浮点数，默认得到的就总是浮点数，即便结果原本为整数。
print(4/2)

# 在书写很大的数时，可使用下划线将其中的位分组，使其更清晰易读：
universe_age = 14_000_000_000
print(universe_age)

###### 2.4.5 同时给多个变量赋值

x,y,z = 1,2,3

# 常量 大写字母表示
MAX_CONNECTIOONS = 5000

print(5 +3)
print(2 * 4)
print(10 -2)
print(56/7)

number = 5
print(f'我最喜欢的数字是{number}')



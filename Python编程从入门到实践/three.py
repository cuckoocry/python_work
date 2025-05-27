
# 第三章 列表

## 在Python中，用方括号([​])表示列表，用逗号分隔其中的元素


bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)


print(bicycles[0])
print(bicycles[0].title())
print(bicycles[3].title())

print(bicycles[-1])

message = f'My first bicycle was a {bicycles[0].title()}.'
print(message)

# 修改元素列表
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)


popped = motorcycles.pop()
print(motorcycles)
print(popped)


motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")


# 如果不确定该使用del语句还是pop()方法，下面是一个简单的判断标准：如果要从列表中删除一个元素，且不再以任何方式使用它，就使用del语句；如果要在删除元素后继续使用它，就使用pop()方法。


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
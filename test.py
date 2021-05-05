
fruits = []
for i in range(5):
    fruit = input("과일을 입력하세요")
    fruits.append(fruit)

num = 1
for i in fruits:
    print("{0}번 과일은 {1}입니다".format(num, i))
    num = num+1

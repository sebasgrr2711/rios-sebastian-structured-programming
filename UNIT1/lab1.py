#Code A
grades=[80,90,70]
average=sum(grades)/len(grades)
print(average)

#Code B
def calculate_average(data):
    return sum(data)/len(data)
grades=[80,90,70]
print(calculate_average(grades))

#Code C modificated
numbers = [10, 20, 30, 40, 50]
cubes = list(map(lambda x: x**3, numbers))
print(cubes)


types_of_people = 10
x = f"There are {types_of_people} types of people." #格式化字符串

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)


print("*" * 20)

print("~" * 15)

#下面的部分是额外根据上例进行的例子

body_shapes = 3
a = f"There are {body_shapes} types of women."

slim = "slim"
curvy = "curvy"
average = "average"
b = f"There are {slim}, {curvy}, {average} bodytypes."

print(a)
print(b)

print(f"I said: {a}")
print(f"I also said: '{b}'")

#Make a won for loop

def won_for_loop(iterable):
    iterator = iter(iterable)

    while True:

        try:
            print(next(iterator))
        except StopIteration:
            break
a = [1,2,3,5,6,7,8,9,10]
b = range(1,10)
c = {1,2,3,4,5,6,7,8,9}
d = (1,2,3,4,5,6,7,8,9)
e = {0:1,1:4,5:7}
f = 1
p = won_for_loop(a)
p()


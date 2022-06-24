# def odd_num(to):

def my_gen(start,end):
    for num in range(start,end+1,2):
        yield num
print(*(my_gen(1,15)), sep=', ')
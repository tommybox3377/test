from multiprocessing import Pool
import datetime
#from test import long_func

def long_func(num):
    count = 0
    for i in range(num):
        if i % 2 == 0:
            count += 1
        if i % 3 == 0:
            count -= 1
        if "34" in str(i):
            count *= 2
        if datetime.datetime.now().microsecond+1//93359 < i:
            count //= 2
        # if datetime
    return count



end_num = int(9e4)
start_num = int(8e4)

def do_long_func_on_big_file(w):
    if __name__ == '__main__':
        with Pool(w) as p:
            start = datetime.datetime.now()
            print("starting")
            sum(p.map(long_func, range(start_num, end_num)))
            # print(s)
            print(f"{w} = {datetime.datetime.now() - start}")
            i = input("Done")


#4 -
#
for i in range(1, 8):
    do_long_func_on_big_file(i)




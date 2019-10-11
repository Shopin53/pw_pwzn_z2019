def task_1():
    for elem 0:1:9
        for z 0:1:elem
	        k+=elem
        k+="\n"

    return k


assert task_1() == '''
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''

def check_frequency(input):
    """
    Perform counting based on input queries and return queries result.

    Na wejściu otrzymujemy parę liczb całkowitych - operacja, wartość.
    Możliwe operacje:
    1, x: zlicz x
    2, x: usuń jedno zliczenie x jeżeli występuje w zbiorze danych
    3, x: wypisz liczbę zliczeń x (0 jeżeli nei występuje)
    Do parsowania wejścia wykorzystaj funkcję parse_input.
    Po wejściu (już jakoliście) iterujemy tylko raz (jedna pętla).
    Zbiór danych zrealizuj za pomocą struktury z collections.

    :param input: pairs of int: command, value
    :type input: string
    :return: list of integers with results of operation 3
    :rtype: list
    """
    def strr(lists):
        return list(map(int,lists))
    inttab=input.strip().splitlines()
    tab_of_tabs=list(map(lambda line: line.split(' '),inttab))    
    final_tab=list(map(strr,tab_of_tabs))
    final=final_tab
    
    listt=[]
    ret=[]
    for i, j in final:
        if i==1:
            listt.append(j)
        #if i==2:
         #   if j in listt:
               # listt.pop(j)
        if i==3:
            ret.append(listt.count(j))
            print(listt.count(j))
    return ret
    
    
_input = """
1 5
1 6
2 1
3 2
1 10
1 10
1 6
2 5
3 5


"""
if __name__ == '__main__':
    assert check_frequency(_input) == [0, 1]
def parse_input(input):
    """
    Splits multiline string into list of lists with integers.

    Napisz funkcję przymującą wielolinijkowy ciąg znaków.
    a zwracającą listę list liczb całkowitych znajdujących się w podanym ciągu znaków.
    Nie używaj pętl for i while.
    String może zawierać puste linie na początku i końcu.

    :param input: string to parse
    :type input: str
    :return: list of parsed list of integers
    :rtype: list
    """
    def strr(lists):
        return list(map(int,lists))
    inttab=input.strip().splitlines()
    tab_of_tabs=list(map(lambda line: line.split(' '),inttab))    
    final_tab=list(map(strr,tab_of_tabs))
    final=final_tab
    return final
        

_input = """
    1 5
    1 6 7
    3 2
    1 10
    1 10
    1 6
    2 5
    3 2
    """ 
if __name__ == '__main__':
    assert parse_input(_input) == [[1, 5], [1, 6, 7], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]
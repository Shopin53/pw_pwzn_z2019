def stack_operation(stack_commands):
    """
    Funkcja przyjmuję listę jedno i dwu elementowych krotek - operacji na stosie.
    Pierwszy element krotki to operacja, drugi wartość (opcjonalnie). Operacje:
    push - dodaj element do stosu
    pop - usuń element ze stosu
    show_max - wypisz maksymalny element w stosie
    Uzupełnij funkcje tak, by dla podanej zwróciła ciąg maksymalnych elementów (zgodny z liczbą operacj 3).

    :param stack_commands: List of tuples of stack commands.
    :type stack_commands: list
    :return: List of outputs from commands.
    :rtype: list
    """
    
    
    pass
    v=[]
    i=0
    while i<len(stack_commands):
        q=stack_commands[i]
        if q[0]=='push':
            v.append(q[1])
        if q[0]=='pop':
            v.pop()
        if q[0]=='show_max':
           len(v)
        i+=1
    return 	v


if __name__ == "__main__":
    commands = [
        ('push', 97),
        ('pop',),
        ('push', 20), 
        ('pop',), 
        ('push', 26), 
        ('push', 20), 
        ('pop',), 
        ('show_max',), 
        ('push', 91), 
        ('show_max',)
    ]
    assert stack_operation(commands) == [26, 91]

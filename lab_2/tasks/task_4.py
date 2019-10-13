def count_letters(msg):
    """
    Zwraca pare (znak, liczba zliczeń) dla najczęściej występującego znaku w wiadomości.
    W przypadku równości zliczeń wartości sortowane są alfabetycznie.

    :param msg: Message to count chars in.
    :type msg: str
    :return: Most frequent pair char - count in message.
    :rtype: list
    """
    pass
    v=[]
    for i in range(97,123):
        v.append(chr(i))
    cout=[]
    s=0
    w='a'
    for i in range(97,123):
        cout.append(msg.count(chr(i)))
        if msg.count(chr(i))>s:
            s=msg.count(chr(i))
            w=chr(i)
    re=[w,s]
    return re
    


if __name__ == '__main__':
    msg = 'Abrakadabra'
    assert count_letters(msg) == ['a', 4]
    assert count_letters('za') == ['a', 1]
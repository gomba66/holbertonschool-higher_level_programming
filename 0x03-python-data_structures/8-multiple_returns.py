#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        len_tot = len(sentence)
        firts = None
    else:
        len_tot = len(sentence)
        first = sentence[0]
    return (len_tot, first)

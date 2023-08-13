#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if leng == 0:
        results = (0, None)
        return results
    else:
        res = (leng, sentence[0:1])
        return res

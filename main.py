import os, io
import recognize_handwriting as rh
import sentence_similarity as ss1
import grammar_check as gc


def evaluate(x, y):
    x = rh.recognize(x)
    y = rh.recognize(y)
    sementic_score = ss1.similarity_score(x, y)
    grammar_errors = gc.check(x)
    return [sementic_score, grammar_errors]

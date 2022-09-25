# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

txt = 'input_1_task.txt'
_trg = 'абв'
res = None
with open(txt, 'r') as fr:
    res = [word for word in fr.read().split() if not _trg in word]
with open('result_1.txt', 'w') as wrt: wrt.write(' '.join(res))


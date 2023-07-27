import random

def most(n: int, str_list: list):
    result = []
    result_num = []
    for i in str_list:
        result.append([i, str_list.count(i)])
    for p in result:
        result_num.append(int(p[1]))
    num_list = sorted(result_num, reverse=True)
    if not num_list:
        return None
    if n >= len(num_list):
        n = len(num_list) - 1

    return result[result_num.index(num_list[n])]

def train(times:int):
    f = open('qwetyuio.txt', 'r', encoding='UTF-8')
    f.close()
    f = open('data.txt', 'r', encoding='UTF-8')
    question = [i for i in f]
    question_answer = []
    for _ in range(times):
        i = random.choice(question)
        for j in i[:i.find(',')].split():
            for k in i[i.find(',')+1:-3].split():
                question_answer.append([j, k])
    return question_answer


answer_list = train(10000)
for _ in range(15):
    question = input('>>> ').split()
    answer = []
    for g in question:
        x = []
        for l in answer_list:
            if l[0] == g:
                x.append(l[1])
        answer.append(most(n=random.randint(0, len(x)), str_list=x))
    answer_main = ""
    answer_last = ""
    for q in answer:
        if '.' in q:
            answer_last += q[0]
            answer_last += " "
            continue
        answer_main += q[0]
        answer_main += " "
    print(answer_main+answer_last)
def machine_learning(time=1000):
    import random
    f = open('data.txt', 'r', encoding='UTF-8')
    cnt = 0
    learning_data = []
    learning_data_2 = []
    for j in f:
        cnt += 1
        if cnt == time:
            break
        learning_data.append(j[j.find(',')+1:-3])
        learning_data_2.append(j[:j.find(',')])
    loss = []
    for _ in learning_data:
        x = random.choice(learning_data_2)
        cnt = len(_)
        for l in range(len(_) if cnt < len(x) else len(x)):
            if _[l] == x[l]:
                cnt -= 1
        loss.append(cnt)
    return min(loss)+4.5
def chat_bot(chat):
    global i
    count = machine_learning(time = 11842)
    f = open('data.txt', 'r', encoding='UTF-8')
    result_1 = []
    result_2 = []
    for i in f:
        x = len(chat)
        for _ in range(len(i[i.find(',')+1:-3]) if len(i[i.find(',')+1:-3]) < len(chat) else len(chat)):
            if chat[_] == i[i.find(',')+1:-3][_]:
                x -= 1
        if x <= count:
         result_1.append(x)
         result_2.append(i[i.find(',')+1:-3])
    try:
        result_2[result_1.index(min(result_1))]
    except ValueError:
        return i
    else:
        return result_2[result_1.index(min(result_1))]


from mtranslate import translate
while True:
    chats = input(">>>")
    if chats == 'quit':
        break
    chats = translate(translate(chats, to_language = 'en'), to_language='ko')
    print(chat_bot(chats))
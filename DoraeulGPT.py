def add_to_tree(tree, words, answer):
    if not words:
        return

    word = words.pop(0)

    if word in tree:
        add_to_tree(tree[word], words.copy(), answer)
    else:
        if words:
            tree[word] = {}
            add_to_tree(tree[word], words.copy(), answer)
        else:
            tree[word] = {"answer": answer}


def get_all_values(tree, prefix=None):
    values = []
    for key, value in tree.items():
        if isinstance(value, dict):
            if prefix:
                values.extend(get_all_values(value, f"{prefix} {key}"))
            else:
                values.extend(get_all_values(value, key))
        elif key == "answer":
            if prefix:
                values.append({prefix: value})
            else:
                values.append({key: value})
    return values


def main():
    questions = []
    answers = []
    tree = {}
    f = open('data.txt', 'r', encoding='UTF-8')

    for i in f:
        questions.append(i[:i.find(',')])
        answers.append(i[i.find(',') + 1:-3].strip())

    for question, answer in zip(questions, answers):
        words = question.split()
        add_to_tree(tree, words, answer)

    all_values = get_all_values(tree)
    print(tree)


if __name__ == "__main__":
    main()

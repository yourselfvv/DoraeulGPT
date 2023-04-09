import time
import googletrans as gt
import webbrowser
from fractions import Fraction
import wikipedia


class ChatBot:
    def __init__(self):pass


    def dip( self , sentence):
        sentence = self.NLP(chats = sentence)
        wordslist = open('qwetyuio.txt', 'r', encoding = 'UTF-8')
        cnt = 0
        for word in range(len(sentence)):
            for line in wordslist:
                cnt = 0
                if len(line) >= 2:
                    for i in range(len(sentence[word]) if len(sentence[word]) < len(line) else len(line)):
                        if line[i] == sentence[word][i]:
                            cnt += 1
                            if cnt >= len(sentence[word]):
                                sentence[word] = line
                                if '안농' in sentence[word]:
                                    sentence[word] = '안녕'
                                break
                    if cnt >= len (sentence[word]):
                        break
        print(sentence)
        return " ".join(sentence)

    def NLP( self , chats ):
        memory = []
        cnat = chats
        if chats.find(' ') == -1:
            return [chats]
        for mem in range(list(cnat).count(' ') + 1):
            memory.append(chats[:chats.find(' ')])
            if ('은' in chats or '는' in chats or '이' in chats or '가' in chats or '로' in chats
                or '를' in chats or '이가' in chats or '을' in chats or '에게' in chats or '께' in chats or '에' in chats):
                if ('은' in chats or '는' in chats or '이' in chats or '가' in chats or '에' in chats
                or '를' in chats or '을' in chats or '께' in chats):
                    memory[mem] = chats[:chats.find(' ') - 1]
                else:
                    memory [ mem ] = chats [ :chats.find (' ') - 2 ]
            chats = chats[chats.find(' ') + 1:]
        return memory

    def coding( self , memory):
        if ('덧셈' in memory or '더하기' in memory or '더해' in memory or '더하' in memory or
            '방정식' in memory or '부등식' in memory or
            '곱셈' in memory or '곱하기' in memory or '곱해' in memory or '곱하' in memory or
            '뺄셈' in memory or '빼기' in memory or '빼주' in memory or '빼는' in memory or
            '나눗셈' in memory or '나누기' in memory or '나누' in memory or '나눠' in memory or
            '계산' in memory):
            print("""def calculator(expression):
    """, end = '')
            time.sleep(0.75)
            print("return eval(expression)")
        elif '구구단' in memory:
            print("for i in range(2, 10):")
            print("    for j in range(1, 10):")
            print('        print(f"{i} * {j} = {i * j})')
        elif '삼각' in memory:
            if '역' in memory:
                print("""for i in range(10,0,-1):
    for j in range(i):
        print("* ",end="")
    print()""")
        else:
            return '이해하지 못했습니다.'

    def worddd(self):
        f = open('qwetyui.txt' , 'r' , encoding= 'UTF-8')
        qwerty = []
        qwe = 0
        while True:
            qwe += 2
            cnt = 0
            words = input(">>> ")
            qwerty.append(words)
            for line in f:
                if str(line[0]) == str(words[-1]) and len(line) >= 2:
                    print(line)
                    qwerty.append(line)
                    cnt += 1
                if cnt == 1:
                    break
            if cnt == 0:
                return 'you win'
            if words == '끝' or len(words) == 1:
                return 'you lose'

    def calculator(self, expression):
        if expression.find("f(x)=") == 0:
            expression_2 = input("::: ")
            if expression_2.find("y") == -1:
                if expression.find("+") != -1:
                    num_f = int(expression[expression.find("+"):len(expression)])
                    num_f2 = int(expression[expression.find("=") + 1:expression.find("+") - 1])
                else:
                    num_f = int(expression[expression.find("-"):len(expression)])
                    num_f2 = int(expression[expression.find("=") + 1:expression.find("-") - 1])
                return num_f2 * int(expression_2[2:len(expression_2) - 1]) + num_f
            if expression_2 == "y=f(x)":
                import turtle
                import tkinter

                def draw_function():
                    turtle.pencolor('red')
                    turtle.pensize(3)
                    expression_lll = []
                    if expression.find("+") != -1:
                        expression_list = expression[expression.find("=") + 1:expression.find("+") - 1]
                        num_f = expression[expression.find("+"):len(expression)]
                    else:
                        expression_list = expression[expression.find("=") + 1:expression.find("-") - 1]
                        num_f = expression[expression.find("-") + 1:len(expression)]
                    expression_lll.append(expression_list)
                    expression_lll.append('*')
                    expression_lll.append('x')
                    expression_lll.append(num_f)
                    formula = "".join(expression_lll)
                    turtle.penup()
                    x = -100
                    y = eval(formula)
                    turtle.goto(x, y)
                    turtle.pendown()

                    for x in range(-100, 101):
                        y = eval(formula)
                        turtle.goto(x, y)

                axis_size = 350
                speed = 0
                turtle.speed(speed)
                turtle.hideturtle()
                for i in range(4):
                    turtle.setheading(90 * i)
                    turtle.forward(axis_size)
                    turtle.home()

                window = turtle.getcanvas()
                frame_title = tkinter.Frame(window)
                frame_title.grid(row=1, column=0)
                frame_bottom = tkinter.Frame(window)
                frame_bottom.grid(row=2, column=0)

                draw_function()
                turtle.mainloop()
                return "finish"
        if expression.find("r") == 0:
            return int(expression[expression.find("t") + 2:len(expression)]) ** 0.5
        if expression.find('y') != -1:
            if expression[0:2] == 'y=':
                import turtle
                import tkinter

                def draw_function():
                    turtle.pencolor('red')
                    turtle.pensize(3)
                    formula = entry_formula.get()
                    turtle.penup()
                    x = -100
                    y = eval(formula)
                    turtle.goto(x, y)
                    turtle.pendown()

                    for x in range(-100, 101):
                        y = eval(formula)
                        turtle.goto(x, y)

                axis_size = 350
                speed = 0
                turtle.speed(speed)
                turtle.hideturtle()
                for i in range(4):
                    turtle.setheading(90 * i)
                    turtle.forward(axis_size)
                    turtle.home()

                window = turtle.getcanvas()
                frame_title = tkinter.Frame(window)
                frame_title.grid(row=1, column=0)
                frame_bottom = tkinter.Frame(window)
                frame_bottom.grid(row=2, column=0)

                label_text = '예: y=2*x+1'
                tkinter.Label(frame_title, text=label_text).grid(row=0, column=0)
                tkinter.Label(frame_bottom, text='y=').grid(row=0, column=0)
                entry_formula = tkinter.Entry(frame_bottom, width=20)
                entry_formula.grid(row=0, column=1, padx=10, pady=10)
                tkinter.Button(frame_bottom, text='그리기', command=draw_function).grid(row=0, column=2)
                turtle.done()
                return "finish"
            else:
                import numpy as np
                expression_down = input("::: ")
                nd = int(expression_down[expression_down.find("x") + 1:expression_down.find('=') - 1])
                nu = int(expression[expression.find("x") + 1:expression.find('=') - 1])
                num_2 = int(expression_down[expression_down.find('=') + 1:len(expression_down)])
                xy = [[int(expression[:expression.find("x")]), nu],
                      [int(expression_down[:expression_down.find("x")]), nd]]
                result = str(np.linalg.solve(xy, [int(expression[expression.find('=') + 1:len(expression)]), num_2]))
                result_list = ['x = ', result[1:result.find(' ')], '  y = ', result[result.find(' ') + 1:len(result) - 1]]
                return "".join(result_list)
        equation = expression.find('=')
        equation_list = []
        expression_1 = expression[0:equation]
        add_1 = expression_1.find("+")
        if equation != -1:
            if not expression.find("<") == -1 and not expression.find(">") == -1:
                if not add_1 == -1:
                    if expression.find('>') != -1 or expression.find('<') != -1:
                        equation_list.append(expression_1[0:add_1 - 1])
                        equation_list.append(expression_1[add_1 + 1:len(expression_1) - 1])
                    else:
                        equation_list.append(expression_1[0:add_1 - 1])
                        equation_list.append(expression_1[add_1 + 1:len(expression_1)])
                else:
                    if not expression_1[0] == '-':
                        add_2 = expression_1.find("-")
                        if expression.find('>') == -1 or expression.find('<') == -1:
                            equation_list.append(expression_1[0:add_2 - 1])
                            equation_list.append(expression_1[add_2:len(expression_1) - 1])
                        else:
                            equation_list.append(expression_1[0:add_2 - 1])
                            equation_list.append(expression_1[add_2:len(expression_1)])
                    else:
                        if expression.find('>') != -1 or expression.find('<') != -1:
                            equation_list.append(expression_1[0:add_1 - 2])
                            equation_list.append(expression_1[add_1 - 1:len(expression_1) - 1])
                        else:
                            equation_list.append(expression_1[0:add_1 - 2])
                            equation_list.append(expression_1[add_1:len(expression_1)])
                expression_2 = expression[equation + 2:len(expression)]
                add_3 = expression_2.find("+")
                if add_3 != -1:
                    equation_list.append(expression_2[0:add_3 - 1])
                    equation_list.append(expression_2[add_3 + 1:len(expression_2)])
                else:
                    if not expression_2[0] == '-':
                        add_3 = expression_2.find("-")
                        equation_list.append(expression_2[0:add_3 - 1])
                        equation_list.append(expression_2[add_3:len(expression_2)])
                    else:
                        equation_list.append(expression_2[0:add_3 - 2])
                        equation_list.append(expression_2[add_3 - 1:len(expression_2)])
            else:
                if not add_1 == -1:
                    if expression.find('>') != -1 or expression.find('<') != -1:
                        equation_list.append(expression_1[0:add_1 - 1])
                        equation_list.append(expression_1[add_1 + 1:len(expression_1) - 1])
                    else:
                        equation_list.append(expression_1[0:add_1 - 1])
                        equation_list.append(expression_1[add_1 + 1:len(expression_1)])
                else:
                    if not expression_1[0] == '-':
                        add_2 = expression_1.find("-")
                        if expression.find('>') == -1 or expression.find('<') == -1:
                            equation_list.append(expression_1[0:add_2 - 1])
                            equation_list.append(expression_1[add_2:len(expression_1) - 1])
                        else:
                            equation_list.append(expression_1[0:add_2 - 1])
                            equation_list.append(expression_1[add_2:len(expression_1)])
                    else:
                        if expression.find('>') != -1 or expression.find('<') != -1:
                            equation_list.append(expression_1[0:add_1 - 2])
                            equation_list.append(expression_1[add_1 - 1:len(expression_1) - 1])
                        else:
                            equation_list.append(expression_1[0:add_1 - 2])
                            equation_list.append(expression_1[add_1:len(expression_1)])
                expression_2 = expression[equation + 1:len(expression)]
                add_3 = expression_2.find("+")
                if add_3 != -1:
                    equation_list.append(expression_2[0:add_3 - 1])
                    equation_list.append(expression_2[add_3 + 1:len(expression_2)])
                else:
                    if not expression_2[0] == '-':
                        add_3 = expression_2.find("-")
                        equation_list.append(expression_2[0:add_3 - 1])
                        equation_list.append(expression_2[add_3:len(expression_2)])
                    else:
                        equation_list.append(expression_2[0:add_3 - 2])
                        equation_list.append(expression_2[add_3 - 1:len(expression_2)])
            x = int(equation_list[0]) - int(equation_list[2])
            num = int(equation_list[3]) - int(equation_list[1])
            if equation != -1:
                if expression.find('>') == -1 and expression.find('<') == -1:
                    if abs(num % x) == 0:
                        if x > 0:
                            return "x = %s" % (num / x)
                        else:
                            return "x = %s" % (num / x)
                    if not abs(num % x) == 0:
                        if x > 0:
                            return "x = %s" % (Fraction(num, x))
                        else:
                            return "x = %s" % (Fraction(num, x))
                else:
                    inequality_1 = expression.find('>')
                    inequality_2 = expression.find('<')
                    if inequality_1 == -1:
                        if abs(num / x) == 0:
                            if x > 0:
                                return "x <= %s" % (num / x)
                            else:
                                return "x >= %s" % (num / x)
                        else:
                            if x > 0:
                                return "x <= %s" % (Fraction(num, x))
                            else:
                                return "x >= %s" % (Fraction(num, x))
                    if inequality_2 == -1:
                        if abs(num / x) == 0:
                            if x > 0:
                                return "x >= %s" % (num / x)
                            else:
                                return "x <= %s" % (num / x)
                        else:
                            if x > 0:
                                return "x >= %s" % (Fraction(num, x))
                            else:
                                return "x <= %s" % (Fraction(num, x))
        if expression.find("<") != -1:
            equation = expression.find('<')
            equation_list = []
            expression_1 = expression[0:equation]
            add_1 = expression_1.find("+")
            if not add_1 == -1:
                equation_list.append(expression_1[0:add_1 - 1])
                equation_list.append(expression_1[add_1 + 1:len(expression_1)])
            else:
                if not expression_1[0] == '-':
                    add_2 = expression_1.find("-")
                    equation_list.append(expression_1[0:add_2 - 1])
                    equation_list.append(expression_1[add_2:len(expression_1)])
                else:
                    equation_list.append(expression_1[0:add_1 - 2])
                    equation_list.append(expression_1[add_1:len(expression_1)])
            expression_2 = expression[equation + 1:len(expression)]
            add_3 = expression_2.find("+")
            if add_3 != -1:
                equation_list.append(expression_2[1:add_3 - 1])
                equation_list.append(expression_2[add_3 + 1:len(expression_2)])
            else:
                if not expression_2[0] == '-':
                    add_3 = expression_2.find("-")
                    equation_list.append(expression_2[1:add_3 - 1])
                    equation_list.append(expression_2[add_3:len(expression_2)])
                else:
                    equation_list.append(expression_2[1:add_3 - 2])
                    equation_list.append(expression_2[add_3 - 1:len(expression_2)])
            x = int(equation_list[0]) - int(equation_list[2])
            num = int(equation_list[3]) - int(equation_list[1])
            if abs(num / x) == 0:
                if x > 0:
                    return "x < %s" % (num / x)
                else:
                    return "x > %s" % (num / x)
            else:
                if x > 0:
                    return "x < %s" % (Fraction(num, x))
                else:
                    return "x > %s" % (Fraction(num, x))
        if expression.find(">") != -1:
            equation = expression.find('>')
            equation_list = []
            expression_1 = expression[0:equation]
            add_1 = expression_1.find("+")
            if not add_1 == -1:
                equation_list.append(expression_1[:add_1 - 1])
                equation_list.append(expression_1[add_1:len(expression_1)])
            else:
                if not expression_1[0] == '-':
                    add_2 = expression_1.find("-")
                    equation_list.append(expression_1[0:add_2 - 1])
                    equation_list.append(expression_1[add_2:len(expression_1)])
                else:
                    equation_list.append(expression_1[0:add_1 - 2])
                    equation_list.append(expression_1[add_1:len(expression_1)])
            expression_2 = expression[equation + 1:len(expression)]
            add_3 = expression_2.find("+")
            if add_3 != -1:
                equation_list.append(expression_2[:add_3 - 1])
                equation_list.append(expression_2[add_3 + 1:len(expression_2)])
            if add_3 == -1:
                if not expression_2[0] == '-':
                    add_3 = expression_2.find("-")
                    equation_list.append(expression_2[0:add_3 - 1])
                    equation_list.append(expression_2[add_3:len(expression_2)])
                else:
                    equation_list.append(expression_2[0:add_3 - 2])
                    equation_list.append(expression_2[add_3 - 1:len(expression_2)])
            x = int(equation_list[0]) - int(equation_list[2])
            num = int(equation_list[3]) - int(equation_list[1])
            if abs(num / x) == 0:
                if x > 0:
                    return "x > %s" % (num / x)
                else:
                    return "x < %s" % (num / x)
            else:
                if x > 0:
                    return "x > %s" % (Fraction(num, x))
                else:
                    return "x < %s" % (Fraction(num, x))
        if expression.find(",") != -1:
            num1 = int(expression[:expression.find(",")])
            num2, data = int(expression[expression.find(",") + 1:len(expression)]), []
            for i in range(1, num1 + 1):
                if (num1 % i == 0) & (num2 % i == 0):
                    data.append(i)
            print("공약수: ", data)
            data1, data2, cam = [], [], []
            for i in range(1, num2 + 1):
                data1.append(i * num1)
            for i in range(1, num1 + 1):
                data2.append(i * num2)
            cnt = 0
            for i in data1:
                if i in data2:
                    cnt += 1
                    cam.append(i)
                    if cnt == 10:
                        break
            return "공배수: %s" % (cam)
        ex = expression.find('=')
        if ex == -1:
            return "%s = %s" % (expression, eval(expression))

    def chat_bot(self, chat):
        import webbrowser
        import playsound as py
        tr = gt.Translator()
        cnt = 0
        xnt = 0
        memory = str(chat)
        expression = []
        en = 'qwertyuiopasdfghjklzxcvbnm'
        for eng in en:
            if eng in chat:
                xnt += 1
        if xnt > 2:
            chat = tr.translate(chat, dest='ko')
            chat = chat.text
        else:
            chat = self.dip(sentence=chat)
        for j in chat:
            for l in range(10):
                if j == str(l):
                    cnt += 1
        if '끝말' in chat:
            return self.worddd()
        elif '프로그램' in chat or '코드' in chat or '코딩' in chat:
            return self.coding(memory=chat)
        elif '불러' in chat:
            return ''
        elif '대해' in chat or '누구야' in chat or '뭐야' in chat:
            if '누구야' in chat:
                qiry = chat[:chat.find('누구야') - 2]
                def who_is ( query ) :
                    try :
                        return wikipedia.summary ( query )
                    except Exception :
                        for new_query in wikipedia.search ( query ) :
                            try :
                                return wikipedia.summary ( new_query )
                            except Exception :
                                pass
                    return "이해하지 못했습니다."

                return tr.translate(who_is(query = tr.translate(qiry, dest = 'en', src = 'auto').text), dest = 'ko', src = 'auto').text
            if '대해' in chat:
                qiry = chat[:chat.find('대해') - 2]

                def who_is ( query ) :
                    try :
                        return wikipedia.summary ( query )
                    except Exception :
                        for new_query in wikipedia.search ( query ) :
                            try :
                                return wikipedia.summary ( new_query )
                            except Exception :
                                pass
                    return "이해하지 못했습니다."

                return tr.translate(who_is ( query = tr.translate ( qiry , dest = 'en' , src = 'auto' ).text ), dest = 'ko', src = 'auto').text
            qiry = chat [ :chat.find ( '뭐야' ) - 1 ]
            def who_is ( query ) :
                try :
                    return wikipedia.summary ( query )
                except Exception :
                    for new_query in wikipedia.search ( query ) :
                        try :
                            return wikipedia.summary ( new_query )
                        except Exception :
                            pass
                return "이해하지 못했습니다."

            return tr.translate(who_is ( query = tr.translate ( qiry , dest = 'en' , src = 'auto' ).text ), dest = 'ko', src = 'auto').text
        elif '가우스' in chat:
            if '소수' in chat:
                if '증명' in chat:
                    return """해석적 증명의 개략:
수론적 함수인 소수 계량 함수의 점근적 성장은 리만 제타 함수를 통해 복소해석학적인 명제로 치환할 수 있다. 우선, 다음과 같은 동치 관계는 초등적으로 보일 수 있다.
\pi(x)\sim x\Leftrightarrow\psi(x)\sim x\Leftrightarrowfrac1{x^2}\int_1^x\psi(x')\,dx'=frac1{x^2}\sum_{n\le x}(x-n)\Lambda(n)\simfrac12
여기서
\psi(x)=\sum_{n\le x}\Lambda(n)
는 제2종 체비쇼프 함수이며,
\Lambda(n)는 폰 망골트 함수이다. 반면, 리만 제타 함수의 로그 도함수는 다음과 같이 쓸 수 있다.
frac{\zeta'(z)}{\zeta(z)} = - \sum_{n =1}^{\infty}frac{\Lambda(n)}{n^z}
두 합을 서로 연관짓기 위해, 다음과 같은 복소해석학적 보조정리를 사용한다.
frac1{2\pi i}\int_{c-\infty i}^{c+\infty i}frac{(x/n)^zdz}{z(z+1)}=begin{cases}1-n/x&n\le x0&n>x\end{cases}\qquad(c>1)
따라서, 제타 함수와 체비쇼프 함수를 다음과 같이 연관지을 수 있다.
frac1{x^2}\int_1^x\psi(x')\,dx' = -frac{1}{2\pi i} \int_{c - \infty i}^{c + \infty i} frac{x^{z-1}}{z(z+1)}frac{\zeta'(z)}{\zeta(z)}\,dz\qquad(c>1)
이제, 우변이 
∞x/to\infty 극한에서 1/2로 수렴함을 경로적분법으로 증명할 수 있다.[2]"""
        elif '오일러' in chat:
            if '식' in chat:
                return '''e^(pi*i)+1=0
[증명] 함수 g(x)를 다음과 같이 정의한다.
g(x)=e^{{ix}}
허수단위 
i는 상수이므로 
g(x)의 도함수와 이계도함수는 다음과 같다.
{begin{aligned}g'(x)&=ie^{{ix}}g''(x)&=i^{2}e^{{ix}}=-e^{{ix}}\end{aligned}}
이로부터
g''(x)=-g(x)\  또는
g''(x)+g(x)=0\  라는 2차 선형 미분방정식이 만들어지고,
일차 독립인 두 해가 발생한다.
{begin{aligned}g_{1}(x)&=\cos xg_{2}(x)&=\sin x\end{aligned}}
한편, 차수가 같은 미분방정식의 어떤 선형 결합도 해가 될 수 있으므로 위의 미분방정식의 일반적인 해는 다음과 같다.
{begin{aligned}g(x)&=Ag_{1}(x)+Bg_{2}(x)&=A\cos x+B\sin xg'(x)&=-A\sin x+B\cos x\end{aligned}}
A와 
B는 상수)
그리고 여기에 함수 
g(x) 의 초기 조건
{begin{aligned}g(0)&=e^{{i0}}&=1g'(0)&=ie^{{i0}}&=i\end{aligned}} 을 대입하면,
{begin{aligned}g(0)&={\color {White}-}A\cos 0+B\sin 0&=Ag'(0)&=-A\sin 0+B\cos 0&=B\end{aligned}}
곧,
{begin{aligned}g(0)&=A&=1g'(0)&=B&=i\end{aligned}}
이므로
g(x)\,=\,e^{{ix}}=\cos x+i\sin x이다.'''
        elif '삼각' in memory and '넓' in memory:
            if memory.find('높이') != -1:
                if memory.find('높이') < memory.find('변'):
                    h = memory[memory.find('높이') + 3:memory.find('c')]
                    memory = memory[memory.find('c') + 2:len(memory)]
                    s = memory[memory.find('변') + 3:memory.find('c')]
                else:
                    h = memory[memory.find('변') + 3:memory.find('c')]
                    memory = memory[memory.find('c') + 2:len(memory)]
                    s = memory[memory.find('높이') + 3:memory.find('c')]
                return "넓이: %s" % (int(s) * int(h) / 2)
        elif '사각' in memory:
            if '사각' in memory and '넓' in memory:
                if memory.find('높이') != -1:
                    if memory.find('높이') < memory.find('변'):
                        h = memory[memory.find('높이') + 3:memory.find('c')]
                        memory = memory[memory.find('c') + 2:len(memory)]
                        s = memory[memory.find('변') + 3:memory.find('c')]
                    else:
                        h = memory[memory.find('변') + 3:memory.find('c')]
                        memory = memory[memory.find('c') + 2:len(memory)]
                        s = memory[memory.find('높이') + 3:memory.find('c')]
                    return "넓이: %s" % (int(s) * int(h))
        elif '원' in chat:
            if '넓' in chat:
                if '지름' in chat:
                    if '반' in chat:
                        if 'cm' in chat:
                            r = int(chat[chat.find('름') + 3:chat.find('원') - 4])
                            return "%sπcm²" % (r ** 2)
                        else:
                            r = int(chat[chat.find('름') + 3:chat.find('원') - 2])
                            return "%sπ" % (r ** 2)
                    else:
                        if 'cm' in chat:
                            r = int(chat[chat.find('름') + 3:chat.find('원') - 4])
                            return "%sπcm²" % ((r / 2) ** 2)
                        else:
                            r = int(chat[chat.find('름') + 3:chat.find('원') - 2])
                            return "%sπ" % ((r / 2) ** 2)
            else:
                if '지름' in chat:
                    if '반' in chat:
                        if 'cm' in chat:
                            r = int(chat[chat.find('름') + 3:chat.find('원') - 4])
                            return "%sπcm" % (r * 2)
                        else:
                            r = int(chat[chat.find('름') + 3:chat.find('원') - 2])
                            return "%sπ" % (r * 2)
                    else:
                        if 'cm' in chat:
                            r = int(chat[chat.find('름') + 3:chat.find('원') - 4])
                            return "%sπcm" % (float(r))
                        else:
                            r = int(chat[chat.find('름') + 3:chat.find('원') - 2])
                            return "%sπ" % (float(r))
        elif '어떤수' in memory:
            if '가' in memory:
                memory1 = memory[0:memory.find('가')]
            else:
                memory1 = memory[0:memory.find('는')]
            if '배' in memory1:
                if '두' in memory1:
                    expression.append('2x')
                if '세' in memory1:
                    expression.append('3x')
                if '네' in memory1:
                    expression.append('4x')
                if '다섯' in memory1:
                    expression.append('5x')
                if '여' in memory1:
                    if '섯' in memory1:
                        expression.append('6x')
                    else:
                        expression.append('8x')
                if '일' in memory1:
                    expression.append('7x')
                if '아' in memory1:
                    expression.append('9x')
                if '열' in memory1:
                    expression.append('10x')
            else:
                expression.append('1x')
            if '더' in memory1:
                if '-' in memory1:
                    expression.append("-%s" % (int(memory1[memory1.find('더') - 4:memory1.find('더') - 2])))
                else:
                    expression.append("+%s" % (int(memory1[memory1.find('더') - 4:memory1.find('더') - 2])))
            elif '뺀' in memory1:
                if '-' in memory1:
                    if memory1[memory1.find('뺀') - 4] == '-':
                        expression.append("+%s" % (int(memory1[memory1.find('뺀') - 3:memory1.find('뺀') - 2])))
                    else:
                        expression.append("+%s" % (int(memory1[memory1.find('뺀') - 4:memory1.find('뺀') - 2])))
                else:
                    expression.append("-%s" % (int(memory1[memory1.find('뺀') - 4:memory1.find('뺀') - 2])))
            else:
                expression.append('+ 0')
            if memory.find('가') == -1:
                memory = memory[memory.find('는') + 1:len(memory)]
            else:
                memory = memory[memory.find('가') + 1:len(memory)]
            expression.append('=')
            if '배' in memory:
                if '두' in memory:
                    expression.append('2x')
                if '세' in memory:
                    expression.append('3x')
                if '네' in memory:
                    expression.append('4x')
                if '다섯' in memory:
                    expression.append('5x')
                if '여' in memory:
                    if '섯' in memory:
                        expression.append('6x')
                    else:
                        expression.append('8x')
                if '일' in memory:
                    expression.append('7x')
                if '아' in memory:
                    expression.append('9x')
                if '열' in memory:
                    expression.append('10x')
            else:
                expression.append('1x')
            if '더' in memory:
                if '-' in memory:
                    expression.append("-%s" % (int(memory[memory.find('더') - 4:memory.find('더') - 2])))
                else:
                    expression.append("+%s" % (int(memory[memory.find('더') - 4:memory.find('더') - 2])))
            elif '뺀' in memory:
                if '-' in memory:
                    if memory[memory.find('뺀') - 4] == '-':
                        expression.append("+%s" % (int(memory[memory.find('뺀') - 3:memory.find('뺀') - 2])))
                    else:
                        expression.append("+%s" % (int(memory[memory.find('뺀') - 4:memory.find('뺀') - 2])))
                else:
                    expression.append("-%s" % (int(memory[memory.find('뺀') - 4:memory.find('뺀') - 2])))
            else:
                expression.append('+0')
            expression = "".join(expression)
            return self.calculator(expression=expression)
        elif '공약' in memory:
            if '와' in memory:
                num1 = int(memory[0:memory.find('와')])
            else:
                num1 = int(memory[0:memory.find('과')])
            if '와' in memory:
                num2 = int(memory[memory.find('와') + 2:memory.find('의')])
            else:
                num2 = int(memory[memory.find('과') + 2:memory.find('의')])
            data = []
            for i in range(1, num1 + 1):
                if (num1 % i == 0) & (num2 % i == 0):
                    data.append(i)
            data1 = []
            for j in data:
                data1.append(str(j))
            return ", ".join(data1)
        elif '공배' in memory:
            if '와' in memory:
                num1 = int(memory[0:memory.find('와')])
            else:
                num1 = int(memory[0:memory.find('과')])
            if '와' in memory:
                num2 = int(memory[memory.find('와') + 2:memory.find('의')])
            else:
                num2 = int(memory[memory.find('과') + 2:memory.find('의')])
            data1, data2, cam = [], [], []
            for i in range(1, num2 + 1):
                data1.append(i * num1)
            for i in range(1, num1 + 1):
                data2.append(i * num2)
            cnt = 0
            for i in data1:
                if i in data2:
                    cnt += 1
                    cam.append(str(i))
                    if cnt == 10:
                        break
            return ", ".join(cam)
        elif 'x' in chat and 'y' in chat:
            memory = chat[:chat.find('y')]
            expression = []
            if '배' in memory:
                if '두' in memory:
                    expression.append('2x')
                if '세' in memory:
                    expression.append('3x')
                if '네' in memory:
                    expression.append('4x')
                if '다섯' in memory:
                    expression.append('5x')
                if '여' in memory:
                    if '섯' in memory:
                        expression.append('6x')
                    else:
                        expression.append('8x')
                if '일' in memory:
                    expression.append('7x')
                if '아' in memory:
                    expression.append('9x')
                if '열' in memory:
                    expression.append('10x')
            else:
                expression.append('1x')
            memory = chat[chat.find('y'):chat.find('것')]
            if memory.find('더') != -1:
                expression.append('+')
            if memory.find('뺀') != -1:
                expression.append('-')
            if '배' in memory:
                if '두' in memory:
                    expression.append('2y')
                if '세' in memory:
                    expression.append('3y')
                if '네' in memory:
                    expression.append('4y')
                if '다섯' in memory:
                    expression.append('5y')
                if '여' in memory:
                    if '섯' in memory:
                        expression.append('6y')
                    else:
                        expression.append('8y')
                if '일' in memory:
                    expression.append('7y')
                if '아' in memory:
                    expression.append('9y')
                if '열' in memory:
                    expression.append('10y')
            else:
                expression.append('1y')
            if chat.find('은') != -1:
                if '고' in memory:
                    memory = chat[chat.find('은'):chat.find('고') - 3]
                else:
                    memory = chat[chat.find('은'):chat.find(',') - 4]
            elif '가' in memory:
                if '고' in memory:
                    memory = chat[chat.find('가'):chat.find('고') - 3]
                else:
                    memory = chat[chat.find('가'):chat.find(',') - 4]
            else:
                if '고' in memory:
                    memory = chat[chat.find('이'):chat.find('고') - 3]
                else:
                    memory = chat[chat.find('이'):chat.find(',') - 4]
            expression.append("=%s" % (memory[1:len(memory)]))
            expression1 = "".join(expression)
            if '고' in chat:
                chat = chat[chat.find('고'):len(chat)]
            elif ',' in chat:
                chat = chat[chat.find(','):len(chat)]
            expression = []
            memory = chat[:chat.find('y')]
            if '배' in memory:
                if '두' in memory:
                    expression.append('2x')
                if '세' in memory:
                    expression.append('3x')
                if '네' in memory:
                    expression.append('4x')
                if '다섯' in memory:
                    expression.append('5x')
                if '여' in memory:
                    if '섯' in memory:
                        expression.append('6x')
                    else:
                        expression.append('8x')
                if '일' in memory:
                    expression.append('7x')
                if '아' in memory:
                    expression.append('9x')
                if '열' in memory:
                    expression.append('10x')
            else:
                expression.append('1x')
            memory = chat[chat.find('y'):chat.find('를')]
            if chat.find('더') != -1:
                expression.append('+')
            if chat.find('뺀') != -1:
                expression.append('-')
            if '배' in memory:
                if '두' in memory:
                    expression.append('2y')
                if '세' in memory:
                    expression.append('3y')
                if '네' in memory:
                    expression.append('4y')
                if '다섯' in memory:
                    expression.append('5y')
                if '여' in memory:
                    if '섯' in memory:
                        expression.append('6y')
                    else:
                        expression.append('8y')
                if '일' in memory:
                    expression.append('7y')
                if '아' in memory:
                    expression.append('9y')
                if '열' in memory:
                    expression.append('10y')
            else:
                expression.append('1y')
            if chat.find('은') != -1:
                if '고' in chat:
                    memory = chat[chat.find('은'):chat.find('고') - 4]
                else:
                    memory = chat[chat.find('은'):chat.find(',') - 5]
            elif '가' in chat:
                if '고' in chat:
                    memory = chat[chat.find('가'):chat.find('고') - 4]
                else:
                    memory = chat[chat.find('가'):chat.find(',') - 5]
            else:
                if '고' in chat:
                    memory = chat[chat.find('이'):chat.find('고') - 4]
                else:
                    memory = chat[chat.find('이'):chat.find(',') - 5]
            expression.append("=%s" % (memory[1:len(memory)]))
            expression2 = "".join(expression)
            import numpy as np
            expression = expression1
            expression_down = expression2
            nd = int(expression_down[expression_down.find("x") + 1:expression_down.find('=') - 1])
            nu = int(expression[expression.find("x") + 1:expression.find('=') - 1])
            num_2 = int(expression_down[expression_down.find('=') + 1:len(expression_down)])
            xy = [[int(expression[:expression.find("x")]), nu], [int(expression_down[:expression_down.find("x")]), nd]]
            result = str(np.linalg.solve(xy, [int(expression[expression.find('=') + 1:len(expression)]), num_2]))
            result_list = ['x = ', result[1:result.find(' ')], '  y = ', result[result.find(' ') + 1:len(result) - 1]]
            return "".join(result_list)
        elif '이름' in chat:
            return '저는 천재 입니다'
        elif '살' in chat:
            return '1살'
        elif '안' in chat and '녕' in chat:
            return '안녕하세요'
        elif '번역' in chat:
            en = 'qwertyuiopasdfghjklzxcvbnm'
            for eng in en:
                if eng in chat:
                    xnt += 1
            if xnt > 2:
                str1 = input("text >>> ")
            else:
                str1 = input("번역할 말 >>> ")
            cnt = 0
            for h in en:
                if h in str1:
                    cnt += 1
            if cnt > 18:
                result = tr.translate(str1, dest='ko')
                return str1, f" => {result.text}"
            elif len(str1) - cnt < 5:
                result = tr.translate ( str1 , dest = 'ko' )
                return str1 , f" => {result.text}"
            else:
                result = tr.translate(str1, dest='en', src='auto')
                return str1, f" => {result.text}"
        elif '고백' in chat:
            time.sleep(2)
            f = open( '../pymemo.txt' , 'r' )
            for i in f:
                print(i)
                time.sleep(2)
            f.close()
            return '끝'
        elif '계산기' in chat:
            en = 'qwertyuiopasdfghjklzxcvbnm'
            for eng in en:
                if eng in chat:
                    xnt += 1
            if xnt > 2:
                print('yes.')
            else:
                print('네')
            time.sleep(2.5)
            import tkinter as tk

            root = tk.Tk()
            root.title("Calculator")
            root.geometry("350x500")

            upper_frame = tk.Frame(root, width=400, height=70)
            upper_frame.pack(pady=40)

            down_frame = tk.Frame(root, width=400, height=100)
            down_frame.pack(padx=10, pady=10)

            entry = tk.Entry(upper_frame, width=20, font=("Courier", 18), borderwidth=5)
            entry.pack()
            entry.insert(0, "")

            answer = []

            def button_clicked(number):
                current = entry.get()
                entry.delete(0, tk.END)
                entry.insert(0, str(current) + str(number))
                answer.append(number)

            def button_clear():
                entry.delete(0, tk.END)
                answer.clear()

            def button_add():
                entry.delete(0, tk.END)
                answer.append('+')

            def button_sub():
                entry.delete(0, tk.END)
                answer.append('-')

            def button_mul():
                entry.delete(0, tk.END)
                answer.append('*')

            def button_div():
                entry.delete(0, tk.END)
                answer.append('/')

            def button_equal():
                entry.delete(0, tk.END)
                aa = str(''.join(map(str, answer)))
                entry.insert(0, eval(aa))

            btn7 = tk.Button(down_frame, text='7', padx=15, pady=10, font=("Courier", 15),
                             command=lambda: button_clicked(7))
            btn7.grid(column=0, row=0, padx=5, pady=5)
            btn8 = tk.Button(down_frame, text='8', padx=15, pady=10, font=("Courier", 15),
                             command=lambda: button_clicked(8))
            btn8.grid(column=1, row=0, padx=5, pady=5)
            btn9 = tk.Button(down_frame, text='9', padx=15, pady=10, font=("Courier", 15),
                             command=lambda: button_clicked(9))
            btn9.grid(column=2, row=0, padx=5, pady=5)

            btn4 = tk.Button(down_frame, text='4', padx=15, pady=10, font=("Courier", 15),
                             command=lambda: button_clicked(4))
            btn4.grid(column=0, row=1, padx=5, pady=5)
            btn5 = tk.Button(down_frame, text='5', padx=15, pady=10, font=("Courier", 15),
                             command=lambda: button_clicked(5))
            btn5.grid(column=1, row=1, padx=5, pady=5)
            btn6 = tk.Button(down_frame, text='6', padx=15, pady=10, font=("Courier", 15),
                             command=lambda: button_clicked(6))
            btn6.grid(column=2, row=1, padx=5, pady=5)

            btn1 = tk.Button(down_frame, text='1', padx=15, pady=10, font=("Courier", 15),
                             command=lambda: button_clicked(1))
            btn1.grid(column=0, row=2, padx=5, pady=5)
            btn2 = tk.Button(down_frame, text='2', padx=15, pady=10, font=("Courier", 15),
                             command=lambda: button_clicked(2))
            btn2.grid(column=1, row=2, padx=5, pady=5)
            btn3 = tk.Button(down_frame, text='3', padx=15, pady=10, font=("Courier", 15),
                             command=lambda: button_clicked(3))
            btn3.grid(column=2, row=2, padx=5, pady=5)

            btn_pm = tk.Button(down_frame, text='+/-', padx=5, pady=10, font=("Courier", 15),
                               command=lambda: button_clicked('-'))
            btn_pm.grid(column=0, row=3, padx=5, pady=5)
            btn0 = tk.Button(down_frame, text='0', padx=15, pady=10, font=("Courier", 15),
                             command=lambda: button_clicked(0))
            btn0.grid(column=1, row=3, padx=5, pady=5)
            btn_p = tk.Button(down_frame, text='.', padx=15, pady=10, font=("Courier", 15),
                              command=lambda: button_clicked('.'))
            btn_p.grid(column=2, row=3, padx=5, pady=5)

            btn_mul = tk.Button(down_frame, text='×', padx=15, pady=10, font=("Courier", 15), command=button_mul,
                                bg='orange')

            btn_mul.grid(column=3, row=0, padx=5, pady=5)

            btn_sub = tk.Button(down_frame, text='-', padx=15, pady=10, font=("Courier", 15), command=button_sub,
                                bg='orange')

            btn_sub.grid(column=3, row=1, padx=5, pady=5)

            btn_add = tk.Button(down_frame, text='+', padx=15, pady=10, font=("Courier", 15), command=button_add,
                                bg='orange')

            btn_add.grid(column=3, row=2, padx=5, pady=5)

            btn_div = tk.Button(down_frame, text='÷', padx=15, pady=10, font=("Courier", 15), command=button_div,
                                bg='orange')

            btn_div.grid(column=3, row=3, padx=5, pady=5)

            btn_c = tk.Button(down_frame, text='C', padx=15, pady=10, font=("Courier", 15), command=button_clear,
                              bg='orange')

            btn_c.grid(column=2, row=4, padx=5, pady=5)

            btn_res = tk.Button(down_frame, text='=', padx=15, pady=10, font=("Courier", 15), command=button_equal,
                                bg='orange')
            btn_res.grid(column=3, row=4, padx=5, pady=5)

            root.mainloop()
        elif '콜라츠' in chat:
            time.sleep(0.8)
            print("콜라츠 상수: 정리 수열의 행을 N, 콜라츠 상수를 C라고 표기한다. C는 수열이 이동한 행의 총합이며 이 값은 –(N-1)의 값과 같다. C=이동한 행의 합=-(N-1), " 
                   "C=-(N-1)이 된다. 12n+1 ~ 12n+12의 범위에서. 시작한 행의 값과 콜라츠 상수의 합은 도착한 행의 값이 된다. 시작한 행으로부터 도착한 행을 구하는 식은. " 
                   "N+C=도착한 행의 값=N-(N-1)=N-N+1=1. 12n+1 ~ 12n+12의 범위에서 각 N과 C의 합은 항상 1이 되므로, 모든 행은 1행에 수렴한다는 것이 증명된다, " 
                   "1행의 수는 1에 수렴하므로 모든 수는 1에 수렴한다는 것이 증명된다 ")
        elif '시' in chat and '써줘' in chat:
            f = open('qwwerty.txt', 'r', encoding = 'UTF-8')
            import random
            qwer = random.randint(1, 6441)
            cnt = 0
            qw = 0
            kl = 0
            for q in range(10000):
                for i in f:
                    cnt += 1
                    qwerty = random.randint ( 1945 , 1967 )
                    if cnt >= qwer - 1:
                        for j in range(qwerty, qwerty + 1):
                            if qw >= 2:
                                kl += 1
                                print(i)
                    if str(qwerty) in i:
                        qw += 1
                        if kl > 0:
                            return '-------------'

        elif  '소설' in chat or '이야기' in chat:
            import novel
            print(novel.novel())
        elif '타이' in chat:
            times = int(input("얼만큼? "))
            print(times)
            time.sleep(1)

            def hello(num):
                if num == 0:
                    return num
                print(num - 1)
                time.sleep(1)
                hello(num - 1)

            return hello(times)
        elif '게임' in chat:
            time.sleep(3)
            en = 'qwertyuiopasdfghjklzxcvbnm'
            for eng in en:
                if eng in chat:
                    xnt += 1
            if xnt > 2:
                print('yes.')
            else:
                print("네")

            self.game()
            return "    "
        elif 'ㅋ' in chat or 'ㅎ' in chat:
            time.sleep(2)
            return '뭐가 그렇게 웃긴가요?'
        elif '만화' in chat:
            return '그것으 저작권 침해이기 때문에 할 수 없습니다.'
        elif '노래' in chat:
            time.sleep(3)
            print("네")
            py.playsound("C:\Download\y2mate.com - 노래를 부르면서 삼각함수를 공부하여 보자.mp3")
            return '끝'
        elif '실' in chat and '검' in chat:
            url = 'https://signal.bz/news'
            webbrowser.open(url=url)
            return None
        elif '배고프' in chat or '배가고' in chat or '배고픈' in chat:
            import random
            qwerty = random.randint(1, 4)
            if qwerty == 1:
                return '디저트 드세요'
            elif qwerty == 2:
                return '밥 드세요'
            else:
                return '피자나 치킨 드세요. '
        elif '졸리다' in chat or '졸려' in chat or '졸린데' in chat:
            return '자세요'
        elif '메모' in chat:
            g = open( '../pythontest.txt' , 'r' )
            if '내용' in chat:
                for lin in g:
                    print(lin)
            if '검색' in chat:
                qwer = input()
                for lin in g:
                    if qwer in lin:
                        print(lin)
            g_list = []
            for i in g:
                g_list.append(i)
            g = open( '../pythontest.txt' , 'w' )
            en = 'qwertyuiopasdfghjklzxcvbnm'
            for eng in en:
                if eng in chat:
                    xnt += 1
            if xnt > 2:
                mem = input("text >>>")
            else:
                mem = input("내용 >>> ")
            for j in g_list:
                g.write(j)
            g.write(mem)
            g.close()
            return ' 완료'
        elif '문제' in chat:
            en = 'qwertyuiopasdfghjklzxcvbnm'
            for eng in en:
                if eng in chat:
                    xnt += 1
            if xnt > 2:
                memory = input("problem >>> ")
                memory = tr.translate(memory, dest='ko', src='auto').text
            else:
                memory = input("문제 내용 >>> ")
            expression = []
            if 'x' in chat and 'y' in chat:
                memory = chat[:chat.find('y')]
                expression = []
                if '배' in memory:
                    if '두' in memory:
                        expression.append('2x')
                    if '세' in memory:
                        expression.append('3x')
                    if '네' in memory:
                        expression.append('4x')
                    if '다섯' in memory:
                        expression.append('5x')
                    if '여' in memory:
                        if '섯' in memory:
                            expression.append('6x')
                        else:
                            expression.append('8x')
                    if '일' in memory:
                        expression.append('7x')
                    if '아' in memory:
                        expression.append('9x')
                    if '열' in memory:
                        expression.append('10x')
                else:
                    expression.append('1x')
                memory = chat[chat.find('y'):chat.find('것')]
                if memory.find('더') != -1:
                    expression.append('+')
                if memory.find('뺀') != -1:
                    expression.append('-')
                if '배' in memory:
                    if '두' in memory:
                        expression.append('2y')
                    if '세' in memory:
                        expression.append('3y')
                    if '네' in memory:
                        expression.append('4y')
                    if '다섯' in memory:
                        expression.append('5y')
                    if '여' in memory:
                        if '섯' in memory:
                            expression.append('6y')
                        else:
                            expression.append('8y')
                    if '일' in memory:
                        expression.append('7y')
                    if '아' in memory:
                        expression.append('9y')
                    if '열' in memory:
                        expression.append('10y')
                else:
                    expression.append('1y')
                if chat.find('은') != -1:
                    if '고' in memory:
                        memory = chat[chat.find('은'):chat.find('고') - 3]
                    else:
                        memory = chat[chat.find('은'):chat.find(',') - 4]
                elif '가' in memory:
                    if '고' in memory:
                        memory = chat[chat.find('가'):chat.find('고') - 3]
                    else:
                        memory = chat[chat.find('가'):chat.find(',') - 4]
                else:
                    if '고' in memory:
                        memory = chat[chat.find('이'):chat.find('고') - 3]
                    else:
                        memory = chat[chat.find('이'):chat.find(',') - 4]
                expression.append("=%s" % (memory[1:len(memory)]))
                expression1 = "".join(expression)
                if '고' in chat:
                    chat = chat[chat.find('고'):len(chat)]
                elif ',' in chat:
                    chat = chat[chat.find(','):len(chat)]
                expression = []
                memory = chat[:chat.find('y')]
                if '배' in memory:
                    if '두' in memory:
                        expression.append('2x')
                    if '세' in memory:
                        expression.append('3x')
                    if '네' in memory:
                        expression.append('4x')
                    if '다섯' in memory:
                        expression.append('5x')
                    if '여' in memory:
                        if '섯' in memory:
                            expression.append('6x')
                        else:
                            expression.append('8x')
                    if '일' in memory:
                        expression.append('7x')
                    if '아' in memory:
                        expression.append('9x')
                    if '열' in memory:
                        expression.append('10x')
                else:
                    expression.append('1x')
                memory = chat[chat.find('y'):chat.find('를')]
                if chat.find('더') != -1:
                    expression.append('+')
                if chat.find('뺀') != -1:
                    expression.append('-')
                if '배' in memory:
                    if '두' in memory:
                        expression.append('2y')
                    if '세' in memory:
                        expression.append('3y')
                    if '네' in memory:
                        expression.append('4y')
                    if '다섯' in memory:
                        expression.append('5y')
                    if '여' in memory:
                        if '섯' in memory:
                            expression.append('6y')
                        else:
                            expression.append('8y')
                    if '일' in memory:
                        expression.append('7y')
                    if '아' in memory:
                        expression.append('9y')
                    if '열' in memory:
                        expression.append('10y')
                else:
                    expression.append('1y')
                if chat.find('은') != -1:
                    if '고' in chat:
                        memory = chat[chat.find('은'):chat.find('고') - 4]
                    else:
                        memory = chat[chat.find('은'):chat.find(',') - 5]
                elif '가' in chat:
                    if '고' in chat:
                        memory = chat[chat.find('가'):chat.find('고') - 4]
                    else:
                        memory = chat[chat.find('가'):chat.find(',') - 5]
                else:
                    if '고' in chat:
                        memory = chat[chat.find('이'):chat.find('고') - 4]
                    else:
                        memory = chat[chat.find('이'):chat.find(',') - 5]
                expression.append("=%s" % (memory[1:len(memory)]))
                expression2 = "".join(expression)
                import numpy as np
                expression = expression1
                expression_down = expression2
                nd = int(expression_down[expression_down.find("x") + 1:expression_down.find('=') - 1])
                nu = int(expression[expression.find("x") + 1:expression.find('=') - 1])
                num_2 = int(expression_down[expression_down.find('=') + 1:len(expression_down)])
                xy = [[int(expression[:expression.find("x")]), nu],
                      [int(expression_down[:expression_down.find("x")]), nd]]
                result = str(np.linalg.solve(xy, [int(expression[expression.find('=') + 1:len(expression)]), num_2]))
                result_list = ['x = ', result[1:result.find(' ')], '  y = ',
                               result[result.find(' ') + 1:len(result) - 1]]
                return " ".join(result_list)
            if '삼각' in memory and '넓' in memory:
                if memory.find('높이') != -1:
                    if memory.find('높이') < memory.find('변'):
                        h = memory[memory.find('높이') + 3:memory.find('c')]
                        memory = memory[memory.find('c') + 2:len(memory)]
                        s = memory[memory.find('변') + 3:memory.find('c')]
                    else:
                        h = memory[memory.find('변') + 3:memory.find('c')]
                        memory = memory[memory.find('c') + 2:len(memory)]
                        s = memory[memory.find('높이') + 3:memory.find('c')]
                    return "S = %s" % (int(s) * int(h) / 2)
            elif '사각' in memory:
                if '사각' in memory and '넓' in memory:
                    if memory.find('높이') != -1:
                        if memory.find('높이') < memory.find('변'):
                            h = memory[memory.find('높이') + 3:memory.find('c')]
                            memory = memory[memory.find('c') + 2:len(memory)]
                            s = memory[memory.find('변') + 3:memory.find('c')]
                        else:
                            h = memory[memory.find('변') + 3:memory.find('c')]
                            memory = memory[memory.find('c') + 2:len(memory)]
                            s = memory[memory.find('높이') + 3:memory.find('c')]
                        return "넓이: %s" % (int(s) * int(h))
            elif '원' in chat:
                if '넓' in chat:
                    if '지름' in chat:
                        if '반' in chat:
                            if 'cm' in chat:
                                r = int(chat[chat.find('름') + 3:chat.find('원') - 4])
                                return "%sπcm²" % (r ** 2)
                            else:
                                r = int(chat[chat.find('름') + 3:chat.find('원') - 2])
                                return "%sπ" % (r ** 2)
                        else:
                            if 'cm' in chat:
                                r = int(chat[chat.find('름') + 3:chat.find('원') - 4])
                                return "%sπcm²" % ((r / 2) ** 2)
                            else:
                                r = int(chat[chat.find('름') + 3:chat.find('원') - 2])
                                return "%sπ" % ((r / 2) ** 2)
                else:
                    if '지름' in chat:
                        if '반' in chat:
                            if 'cm' in chat:
                                r = int(chat[chat.find('름') + 3:chat.find('원') - 4])
                                return "%sπcm" % (r * 2)
                            else:
                                r = int(chat[chat.find('름') + 3:chat.find('원') - 2])
                                return "%sπ" % (r * 2)
                        else:
                            if 'cm' in chat:
                                r = int(chat[chat.find('름') + 3:chat.find('원') - 4])
                                return "%sπcm" % (float(r))
                            else:
                                r = int(chat[chat.find('름') + 3:chat.find('원') - 2])
                                return "%sπ" % (float(r))
            elif '어떤수' in memory:
                memory1 = memory[0:memory.find('가')]
                if '배' in memory1:
                    if '두' in memory1:
                        expression.append('2x')
                    if '세' in memory1:
                        expression.append('3x')
                    if '네' in memory1:
                        expression.append('4x')
                    if '다섯' in memory1:
                        expression.append('5x')
                    if '여' in memory1:
                        if '섯' in memory1:
                            expression.append('6x')
                        else:
                            expression.append('8x')
                    if '일' in memory1:
                        expression.append('7x')
                    if '아' in memory1:
                        expression.append('9x')
                    if '열' in memory1:
                        expression.append('10x')
                else:
                    expression.append('1x')
                if '더' in memory1:
                    if '-' in memory1:
                        expression.append("-%s" % (int(memory1[memory1.find('더') - 5:memory1.find('더') - 2])))
                    else:
                        expression.append("+%s" % (int(memory1[memory1.find('더') - 4:memory1.find('더') - 2])))
                elif '뺀' in memory1:
                    if '-' in memory1:
                        expression.append("+%s" % (int(memory1[memory1.find('뺀') - 5:memory1.find('뺀') - 2])))
                    else:
                        expression.append("-%s" % (int(memory1[memory1.find('뺀') - 5:memory1.find('뺀') - 2])))
                else:
                    expression.append('+0')
                memory = memory[memory.find('가') + 1:len(memory)]
                if memory.find('가') == -1:
                    memory = memory[memory.find('는') + 1:len(memory)]
                expression.append('=')
                if '배' in memory:
                    if '두' in memory:
                        expression.append('2x')
                    if '세' in memory:
                        expression.append('3x')
                    if '네' in memory:
                        expression.append('4x')
                    if '다섯' in memory:
                        expression.append('5x')
                    if '여' in memory:
                        if '섯' in memory:
                            expression.append('6x')
                        else:
                            expression.append('8x')
                    if '일' in memory:
                        expression.append('7x')
                    if '아' in memory:
                        expression.append('9x')
                    if '열' in memory:
                        expression.append('10x')
                else:
                    expression.append('1x')
                if '더' in memory:
                    if '-' in memory:
                        expression.append("-%s" % (int(memory[memory.find('더') - 5:memory.find('더') - 2])))
                    else:
                        expression.append("+%s" % (int(memory[memory.find('더') - 5:memory.find('더') - 2])))
                elif '뺀' in memory:
                    if '-' in memory:
                        expression.append("+%s" % (int(memory[memory.find('뺀') - 5:memory.find('뺀') - 2])))
                    else:
                        expression.append("-%s" % (int(memory[memory.find('뺀') - 5:memory.find('뺀') - 2])))
                else:
                    expression.append('+0')
                expression = "".join(expression)
                return self.calculator(expression=expression)
            elif '공약' in memory:
                if '와' in memory:
                    num1 = int(memory[0:memory.find('와')])
                else:
                    num1 = int(memory[0:memory.find('과')])
                num2, data = int(memory[memory.find('과') + 2:memory.find('의')]), []
                for i in range(1, num1 + 1):
                    if (num1 % i == 0) & (num2 % i == 0):
                        data.append(i)
                data1 = []
                for j in data:
                    data1.append(str(j))
                return ", ".join(data1)
            elif '공배' in memory:
                if '와' in memory:
                    num1 = int(memory[0:memory.find('와')])
                else:
                    num1 = int(memory[0:memory.find('과')])
                num2 = int(memory[memory.find('과') + 2:memory.find('의')])
                data1, data2, cam = [], [], []
                for i in range(1, num2 + 1):
                    data1.append(i * num1)
                for i in range(1, num1 + 1):
                    data2.append(i * num2)
                cnt = 0
                for i in data1:
                    if i in data2:
                        cnt += 1
                        cam.append(str(i))
                        if cnt == 10:
                            break
                return ", ".join(cam)
        elif '끝' in chat:
            return None
        else:
            qwertyui = open( '../venv/data.txt' , 'r' , encoding = 'UTF-8' )
            cnt = 0
            for i in qwertyui:
                for j in range(len(chat) - 3):
                    if chat[:j] in i[:i.find(',')]:
                        cnt += 1
                        if cnt > len(chat) / 5:
                            return i[i.find(',') + 1:-3]
                if cnt < 3:
                    cnt = 0
            if cnt == 0:
                return '이해하지 못했습니다.'

    def game(self):
        time.sleep(2)
        webbrowser.open(url='https://classic.minecraft.net/?join=XqbiL2-611QDfn7m')

    def search(self):
        webbrowser.open(url='https://www.google.com')

    def Run(self):

        f1 = open( 'stdout.txt', 'r', encoding = 'UTF-8')
        lists = []
        for line in f1:
            lists.append(line)
        f11 = open( '내꺼.txt', 'r', encoding = 'UTF-8')
        listss = []
        for line in f11:
            listss.append(line)
        f = open( 'stdout.txt', 'w', encoding = 'UTF-8')
        ff = open( '내꺼.txt', 'w', encoding = 'UTF-8')
        for line in listss:
            ff.write(line)
        while True:
            self.chatting = input(" >>> ")
            if '불러' in self.chatting:
                for line in lists:
                    print(line)
                    f.write(line)
                    ff.write(line)
            xnt = 0
            en = 'qwertyuiopasdfghjklzxcvbnm'
            tr = gt.Translator()
            result = self.chat_bot(chat=self.chatting)
            for eng in en:
                if eng in self.chatting:
                    xnt += 1
            if xnt > 5:
                print(tr.translate(result, dest = 'en', src = 'auto').text)
            else:
                print (result)
            if '그만' in self.chatting or '끝' in self.chatting and not '말잇' in self.chatting or '잘가' in self.chatting:
                time.sleep(1)
                break
            f.write(">>> " + self.chatting)
            f.write("""
 """)
            if '콜라츠' in self.chatting:
                f.write("""콜라츠 상수: 정리 수열의 행을 N, 콜라츠 상수를 C라고 표기한다.
C는 수열이 이동한 행의 총합이며 이 값은 –(N-1)의 값과 같다. C=이동한 행의 합=-(N-1),C=-(N-1)이 된다. 12n+1 ~ 12n+12의 범위에서.
시작한 행의 값과 콜라츠 상수의 합은 도착한 행의 값이 된다. 시작한 행으로부터 도착한 행을 구하는 식은 N+C=도착한 행의 값=N-(N-1)=N-N+1=1. 12n+1 ~ 12n+12의 범위에서 각 N과 C의 합은 항상 1이 되므로, 
모든 행은 1행에 수렴한다는 것이 증명된다, 1행의 수는 1에 수렴하므로 모든 수는 1에 수렴한다는 것이 증명된다""")
            else:
                f.write(str(result))
                f.write("""
""")
            ff.write(">>> " + self.chatting)
            ff.write("""
 """)
            if '콜라츠' in self.chatting:
                ff.write ("""콜라츠 상수: 정리 수열의 행을 N, 콜라츠 상수를 C라고 표기한다.
C는 수열이 이동한 행의 총합이며 이 값은 –(N-1)의 값과 같다. C=이동한 행의 합=-(N-1),C=-(N-1)이 된다. 12n+1 ~ 12n+12의 범위에서.
시작한 행의 값과 콜라츠 상수의 합은 도착한 행의 값이 된다. 시작한 행으로부터 도착한 행을 구하는 식은 N+C=도착한 행의 값=N-(N-1)=N-N+1=1. 12n+1 ~ 12n+12의 
범위에서 각 N과 C의 합은 항상 1이 되므로, 
모든 행은 1행에 수렴한다는 것이 증명된다, 1행의 수는 1에 수렴하므로 모든 수는 1에 수렴한다는 것이 증명된다""")
            else:
                ff.write(str(result))
                ff.write("""
""")
        f.close()
        ff.close()


Bot = ChatBot()

Bot.Run()

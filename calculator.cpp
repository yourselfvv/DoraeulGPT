#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int integer(char num);

int integer(char num) {
    int result = 0;
    if (num >= '0' && num <= '9') {
        result = num - '0';
    }
    return result;
}

int One(const char* expression) {
    int i;
    int x_list[] = { 0, 0 };
    int num_list[] = { 0, 0 };
    int cnta = 0;
    int cntb = 0;
    for (i = 0; i < strlen(expression); i++) {
        if (expression[i + 1] == 'x') {
            x_list[cnta] = integer(expression[i]);
            cnta += 1;
            continue;
        }
        if (expression[i] >= '0' && expression[i] <= '9') {
            num_list[cntb] = integer(expression[i]);
            if (i > 0 && expression[i - 1] == '-') {
                num_list[cntb] *= -1;
            }
            cntb += 1;
        }
    }
    if (x_list[0] - x_list[1] != 0) {
        printf("x = %d\n", (-num_list[0] + num_list[1]) / (x_list[0] - x_list[1]));
    }
    else {
        printf("해 없음");
    }
    return 0;
}

int Operator(char c) {
    return (c == '+' || c == '-' || c == '*' || c == '/');
}

int precedence(char operators) {
    if (operators == '+' || operators == '-') {
        return 1;
    }
    else if (operators == '*' || operators == '/') {
        return 2;
    }
    return 0;
}

int apply(int a, int b, char operators) {
    switch (operators) {
    case '+':
        return a + b;
    case '-':
        return a - b;
    case '*':
        return a * b;
    case '/':
        return a / b;
    default:
        return 0;
    }
}

int evaluateExpression(const char* expression) {
    int i;
    int len = strlen(expression);

    int* values = (int*)malloc(len * sizeof(int));
    char* operators = (char*)malloc(len * sizeof(char));

    int valuesTop = -1;
    int operatorsTop = -1;

    for (i = 0; i < len; i++) {
        if (expression[i] == ' ')
            continue;
        else if (isdigit(expression[i])) {
            int value = 0;
            while (i < len && isdigit(expression[i])) {
                value = (value * 10) + (expression[i] - '0');
                i++;
            }
            values[++valuesTop] = value;
            i--;
        }
        else if (Operator(expression[i])) {
            while (operatorsTop != -1 && precedence(operators[operatorsTop]) >= precedence(expression[i])) {
                int b = values[valuesTop--];
                int a = values[valuesTop--];
                char op = operators[operatorsTop--];
                values[++valuesTop] = apply(a, b, op);
            }
            operators[++operatorsTop] = expression[i];
        }
    }

    while (operatorsTop != -1) {
        int b = values[valuesTop--];
        int a = values[valuesTop--];
        char op = operators[operatorsTop--];
        values[++valuesTop] = apply(a, b, op);
    }

    int result = values[valuesTop--];
    free(values);
    free(operators);

    return result;
}

int Two(const char* expression) {
    int result = evaluateExpression(expression);
    printf("Result: %d\n", result);

    return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int Three(const char* expressiono, const char* expressiont) {
    int xo = 0, yo = 0, xt = 0, yt = 0, numo = 0, numt = 0;

    if (expressiono[0] == 'x')
        xo = 1;
    else
        xo = expressiono[0] - '0';

    for (int i = 0; i < strlen(expressiono); i++) {
        if (expressiono[i] == 'y') {
            yo = expressiono[i - 1] - '0';
            break;
        }
    }

    numo = expressiono[strlen(expressiono) - 1] - '0';

    if (expressiont[0] == 'x')
        xt = 1;
    else
        xt = expressiont[0] - '0';

    for (int i = 0; i < strlen(expressiont); i++) {
        if (expressiont[i] == 'y') {
            yt = expressiont[i - 1] - '0';
            break;
        }
    }

    numt = expressiont[strlen(expressiont) - 1] - '0';

    double t_var1[3] = { 0 };
    double t_var2[3] = { 0 };
    double x = 0, y = 0;
    int var1[] = { xo, yo, numo };
    int var2[] = { xt, yt, numt };

    if (var1[0] == 0 && var1[1] == 0)
        return 0;

    if (var2[0] == 0 && var2[1] == 0)
        return 0;

    if (var1[0] == 0 && var2[0] == 0) {
        y = var1[2] / (double)var1[1];
        if (y != (var2[2] / (double)var2[1]))
            return 0;

        printf("y = %lg\n", y);
        return 1;
    }

    if (var1[1] == 0 && var2[1] == 0) {
        x = var1[2] / (double)var1[0];
        if (x != (var2[2] / (double)var2[0]))
            return 0;

        printf("x = %lg\n", x);
        return 1;
    }

    for (int i = 0; i < 3; i++) {
        t_var1[i] = var1[i] * var2[0];
        t_var2[i] = var2[i] * var1[0];
    }

    if (var1[0] != 0) {
        y = (t_var2[2] - t_var1[2]) / (t_var2[1] - t_var1[1]);
        x = (var1[2] - var1[1] * y) / (double)var1[0];
    }
    else {
        y = var1[2] / (double)var1[1];
        x = (var2[2] - var2[1] * y) / (double)var2[0];
    }

    printf("\n방정식 해>>\n");
    printf("x = %lg\n", x);
    printf("y = %lg\n", y);

    return 0;
}

int main(void) {
    char expression[100];
    printf(">>>");
    scanf_s("%s", expression, sizeof(expression));
    puts("");
    int cnt = 0; int i;
    for (i = 0; i <= strlen(expression); i++) {
        if (expression[i] == 'x') {
            cnt++;
        }
        if (expression[i] == 'y') {
            cnt+=5;
        }
    }
    if (cnt == 2) {
        One(expression);
    }
    if (cnt == 0) {
        Two(expression);
    }
    if (cnt == 6) {
        char expressiont[100];
        printf(">>>");
        scanf_s("%s", expressiont, sizeof(expressiont));
        puts("");
        Three(expression, expressiont);
    }
    return 0;
}

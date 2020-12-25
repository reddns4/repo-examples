# Условие
# В файловую систему одного суперкомпьютера проник вирус, который сломал 
# контроль за правами доступа к файлам. Для каждого файла известно, с какими 
# действиями можно к нему обращаться:

# запись W,
# чтение R,
# запуск X.
# В первой строке содержится число N — количество файлов содержащихся в данной
# файловой системе. В следующих N строчках содержатся имена файлов и допустимых
# с ними операций, разделенные пробелами. Далее указано чиcло M — количество
# запросов к файлам. В последних M строках указан запрос вида Операция Файл.
# К одному и тому же файлу может быть применено любое колличество запросов.

# Вам требуется восстановить контроль над правами доступа к файлам 
# (ваша программа для каждого запроса должна будет возвращать OK если 
# над файлом выполняется допустимая операция, или же Access denied, если 
# операция недопустима.

# 4
# helloworld.exe R X
# pinglog W R
# nya R
# goodluck X W R
# 5
# read nya
# write helloworld.exe
# execute nya
# read pinglog
# write pinglog

# A:
# OK
# Access denied
# Access denied
# OK
# OK

permission = {}

n = int(input())
for _ in range(n):
    s = input().split()
    file, perm = s[0], set(s[1:])
    permission[file] = perm

m = int(input())
for _ in range(m):
    s = input().split()
    perm, file  = s[0], s[1]

    if perm == 'read':
        perm = 'R'
    elif perm == 'write':
        perm = 'W'
    elif perm == 'execute':
        perm = 'X'

    if perm in permission[file]:
        print('OK')
    else:
        print('Access denied')



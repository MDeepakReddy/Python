import colorama

colorama.init()
RESET = '\u001b[0m'
print('\u001b[30m', "hello black", RESET)
print('\u001b[31m', "hello red", RESET)
print('\u001b[32m', "hello green", RESET)
print('\u001b[33m', "hello yellow", RESET)
print('\u001b[34m', "hello blue", RESET)
print('\u001b[35m', "hello magenta", RESET)
print('\u001b[36m', "hello cyan", RESET)
print('\u001b[37m', "hello white", RESET)
print('\u001b[1m', "hello bold", RESET)
print('\u001b[4m', "hello underline", RESET)
print('\u001b[7m', "hello reverse", RESET)
colorama.deinit()

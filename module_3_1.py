calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() == i.lower() and string.upper() == i.upper():
            return True
    return False


res = string_info('Capybara')
res2 = string_info('Armageddon')
res3 = is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
res4 = is_contains('cycle', ['recycle', 'cyclic'])
print(res)
print(res2)
print(res3)
print(res4)
print(calls)

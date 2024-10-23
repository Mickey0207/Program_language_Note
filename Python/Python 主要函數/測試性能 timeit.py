#timeit.timeit(stmt, setup,timer, number)

# stmt      要測試的程式或語句 "pass"
# setup     運行 stmt 前的語句，純文本，預設是 "pass"
# timer     計時器，一般都會忽略
# number    stmt 執行的次數，預設是 1000000

import timeit

list_test = timeit.timeit(stmt = "[1,2,3,4,5]", number = 10000000)
print("list time is", list_test)
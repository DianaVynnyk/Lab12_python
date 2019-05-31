import re

def count_operations():
    #pattern = r"17/May/2015:(20|1[0-9]|0[1-9]):\d\d.+GET.+presentations.+200"
    pattern = r".*WFLYCTL.*ERROR.*"
    file = open("server.log.2018-04-04", "r")
    counter = 0
    count = 0
    for line in file.readlines():
        count += 1
        if re.search(pattern, line):
            counter += 1
            print(line)
    print(count)
    print(counter)

count_operations()
print(count_operations)
            

__author__ = 'gregorylevin'

def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1

        return found

testlist = ["friendly", "warm", "cute"]

print(sequentialSearch(testlist, "cute"))
print(sequentialSearch(testlist, 13))

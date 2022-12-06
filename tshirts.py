def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    elif cms == 38:
        return ''
    else:
        return 'L'

assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')
assert(size(38) == ''), "Size of the T-shirt cannot be classified"
assert(size(42) == 'L'), "Size of the T-shirt should be L"
print("All is well (maybe!)\n")

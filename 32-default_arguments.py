# default arguments = A default value for certain parameters 
#                      a default argument is used when that argument is omitted
#                      make your function more flexible, reduces # of arguments
#               1-positional, 2- default, 3- keyword, 4- arbitrary

def net_price(list_price, discount=0, tax= 0.05):
    retur (list_price * (1-discount)*(1+tax))


# if not provided arg uses de default value. no need to give all args
# 1 arg
# print(net_price(500)) 1 
# 2 arg
# print(net_price(500, 0.1))
# 3 arg
# print(net_price(500, 0.1, 0))

#default args should be after positional args
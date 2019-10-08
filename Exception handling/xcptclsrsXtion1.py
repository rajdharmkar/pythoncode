try:
    a = john
except:
    try:
        4/0
    except:
        pass
    raise
# code try-except block in except clause raises exception the original NameError in first code is not raised...
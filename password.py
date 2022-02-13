x = 2
while x >= 0:
    password = input('請輸入密碼')
    if password == 'abc123':
        print('登入成功')
        x = -1
    elif password != 'abc123':
        print ('登入失敗')
        if x == 0:
            print('沒有機會了')
        else:
            print ('還有', x,'次機會')
        x = x - 1



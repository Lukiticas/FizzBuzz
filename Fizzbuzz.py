def fizz_buzz_maker():
    for i in range(1, 101):
        st = ''
        if not i % 3 and not i % 5:
            st += 'FizzBuzz'
        elif not i % 3:
            st += 'fizz'
        elif not i % 5:
            st += 'buzz'
        else:
            st = i
        print(st) 
        
fizz_buzz_maker()

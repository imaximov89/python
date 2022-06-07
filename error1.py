
while True:
    try:
        age = int(input('what is your age?\n'))
        10/age
#        raise ValueError('What are you doing?')
    except ValueError:
        print('Enter a number.')
    except ZeroDivisionError:
        print('Cannot be 0')
    else:
        print('Thank you.')
        break
    finally:
        print('Finally done.')

          
def convert_to_mandarin(n):
    n = int(n)
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    if n >= 0 and n <= 10:
        return trans[str(n)]
    elif n > 10 and n < 20:
        return 'shi ' + trans[str(n - 10)]
    elif n >= 20 and n < 100:
        if n % 10 == 0:
            return trans[str(int(n/10))] + ' shi'
        else:
            return trans[str(int(n/10))] + ' shi ' + trans[str(n % 10)]
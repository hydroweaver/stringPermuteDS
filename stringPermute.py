x = 0

def shifter(s, start=0):
        global x
        global level
        s = list(s)
        l = len(s)
        if start == l-1:
            x += 1
            print('Printing Line : %s' % s)
        else:
            for i in range(start, l):
                print('Current s is %s and i is %d' % (s[i], i))
                s[start], s[i] = s[i], s[start]
                print('Go Deeper')
                shifter(s, start+1)
                print('Come out')

shifter('abc')

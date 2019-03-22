import turtle as t
from sys import argv

def main():
    if len(argv) != 2:
        print('ERROR: no arguments given')
        print('try \'python drawer.py xxx.tk xxx.rl\'')
        return
    
    trackfile = argv[0]
    linefile = argv[1]

    if trackfile[-3:0] != '.tk':
        print('ERROR: wrong track file format, should be *.tk')
        return
    if linefile[-3:0] != '.rl':
        print('ERROR: wrong racingline file format, should be *.rl')
        return
    
    



if __name__ == '__main__':
    main()

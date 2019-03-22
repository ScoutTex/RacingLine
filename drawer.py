import turtle as t
from sys import argv

def main():
    if len(argv) != 2:
        print('ERROR: no arguments given')
        print('try \'python drawer.py xxx.tk xxx.rl\'')
        return
    
    track = argv[0]
    line = argv[1]

    if track[-3:0] != '.tk':
        print('ERROR: wrong track file format, should be *.tk')
        return
    if line[-3:0] != '.rl':
        print('ERROR: wrong racingline file format, should be *.rl')
        return
    
    


if __name__ == '__main__':
    main()

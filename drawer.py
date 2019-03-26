from turtle import setup, setworldcoordinates, goto, penup, pendown, left, forward, setheading
from turtle import colormode, fillcolor, pencolor, begin_fill, end_fill, pensize, done
from track import Track
from racingline import Racingline
from sys import argv


class Drawer:
    track_file = ''
    racingline_files = []

    tk = Track()
    rls = []

    def is_track_file(self, track_file):
        if track_file[-3:] != '.tk':
            print('ERROR: wrong track file format, should be *.tk')
            return False
        else:
            return True

    def is_racingline_file(self, racingline_file):
        if racingline_file[-3:] != '.rl':
            print('ERROR: wrong racingline file format, should be *.rl')
            return False
        else:
            return True

    def __init__(self, track_file='', racingline_files=[]):
        if self.is_track_file(track_file):
            self.track_file = track_file
            self.tk = Track(self.track_file)
        for racingline_file in racingline_files:
            if self.is_racingline_file(racingline_file):
                self.racingline_files.append(racingline_file)
        colormode(255)

    def draw_rct(self, r):
        goto(r.left, r.bot)
        pendown()
        setheading(0)
        begin_fill()
        forward(r.width)
        left(90)
        forward(r.height)
        left(90)
        forward(r.width)
        left(90)
        forward(r.height)
        end_fill()
        penup()

    def draw(self):
        setup(self.tk.race_area.width, self.tk.race_area.height)
        setworldcoordinates(0, 0, self.tk.race_area.width, self.tk.race_area.height)
        pensize(3)
        penup()
        pencolor('#333333')
        fillcolor('#66ff66')
        for b in self.tk.barriers:
            self.draw_rct(b)
        pencolor('#333333')
        fillcolor('#ff6666')
        self.draw_rct(self.tk.goal_area)
        done()


def main():
    if len(argv) < 1:
        print('ERROR: no arguments given')
        print('try \'python drawer.py xxx.tk xxx.rl\'')
        return
    else:
        d = Drawer(argv[0], argv[1:])
        d.draw()


if __name__ == '__main__':
    main()

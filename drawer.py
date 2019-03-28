from turtle import setup, setworldcoordinates, goto, penup, pendown, left, right, forward, setheading
from turtle import colormode, fillcolor, pencolor, begin_fill, end_fill, pensize, done, circle, speed
from track import Track
from racingline import Racingline
from sys import argv


class Drawer:
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

    def __init__(self, track_file='', racingline_files=[], speed=3):
        if self.is_track_file(track_file):
            self.tk = Track(track_file)
        for racingline_file in racingline_files:
            if self.is_racingline_file(racingline_file):
                self.rls.append(Racingline(racingline_file))
        self.default_speed = speed
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

    def draw_cir(self, radius=4, fill_color=''):
        right(90)
        forward(radius)
        left(90)
        if len(fill_color) > 0:
            fillcolor(fill_color)
        begin_fill()
        circle(radius)
        end_fill()
        left(90)
        forward(radius)
        right(90)

    def draw_rl(self, start_point, rl, line_color='#6699ff', point_color='#000000'):
        goto(start_point.left, start_point.bot)
        pencolor(line_color)
        fillcolor(point_color)
        pendown()
        angle, rate = rl.start.angle, rl.start.rate
        setheading(angle)
        forward(rate)
        for s in rl.step:
            angle += s.angle
            rate += s.rate
            setheading(angle)
            forward(rate)
        penup()

        speed(0)
        goto(start_point.left, start_point.bot)
        angle, rate = rl.start.angle, rl.start.rate
        pencolor(point_color)
        fillcolor(point_color)
        self.draw_cir(4)
        forward(rate)
        self.draw_cir(4)
        for s in rl.step:
            angle += s.angle
            rate += s.rate
            setheading(angle)
            forward(rate)
            self.draw_cir(4)
        speed(self.default_speed)

    def draw(self):
        setup(self.tk.race_area.width, self.tk.race_area.height)
        setworldcoordinates(0, 0, self.tk.race_area.width, self.tk.race_area.height)
        speed(self.default_speed)
        pensize(3)
        penup()
        pencolor('#333333')
        fillcolor('#66ff66')
        for b in self.tk.barriers:
            self.draw_rct(b)
        pencolor('#333333')
        fillcolor('#ff6666')
        self.draw_rct(self.tk.goal_area)
        for rl in self.rls:
            self.draw_rl(self.tk.start_point, rl)
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

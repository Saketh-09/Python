from tkinter.tix import MAX


def game():
    MAX_STONES=100
    MIN_STONES=5
    while MAX_STONES>=MIN_STONES:
        p1=int(input('Player 1:Enter stone number between 1 & 5: '))
        while p1<1 or p1>5:
            p1=int(input('Invalid entry,please re-enter only stone numbers between 1 & 5: '))
        
        p2=int(input('Player 2:Enter stone number between 1 & 5: '))
        while p2<1 or p2>5:
            p2=int(input('Invalid entry,please re-enter only stone numbers between 1 & 5: '))
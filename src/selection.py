# unavailable on windows! pip install windows-curses
import curses

class Selection():
    def selection(self, stdscr, prompt:str, classes:list, selected:str, no_hint:bool):
        attributes = {}
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        attributes['normal'] = curses.color_pair(1)

        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        attributes['highlighted'] = curses.color_pair(2)

        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
        attributes['cyan'] = curses.color_pair(3)

        c = 0  # last character read
        option = 0  # the current option that is marked
        while c != 10:  # Enter in ascii
            stdscr.erase()
            stdscr.addstr(prompt, attributes["cyan"])
            if not no_hint:
                stdscr.addstr(" >> Use arrow keys to select and then press RETURN")
            stdscr.addstr("\n")
            for i in range(len(classes)):
                if i == option:
                    attr = attributes['highlighted']
                    stdscr.addstr(selected, attr)
                else:
                    attr = attributes['normal']

                stdscr.addstr(classes[i] + "\n", attr)
            c = stdscr.getch()
            if (c == curses.KEY_UP and option > 0) or (c == curses.KEY_LEFT and option > 0):
                option -= 1
            elif (c == curses.KEY_DOWN and option < len(classes) - 1) or (c == curses.KEY_RIGHT and option < len(classes) - 1):
                option += 1

        self.choice = classes[option]

    def __init__(self, prompt:str, options:list, selected="> ", no_hint=False) -> None:
        curses.wrapper(self.selection, prompt, options, selected, no_hint)

        curses.endwin()
    
    def __repr__(self):
        return self.choice
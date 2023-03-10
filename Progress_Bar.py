from math import ceil,floor
#from Cur_pos import cursorPos
import os,time,sys;os.system("")

def move(x, y):
	print("\033[%d;%dH" % (y, x),end="")

print("🚀⚜☢☣🔰💠‣※¤⨠⫸")

def Progress_Bar(NUMBER,preffix="",suffix=""):
    #x,y = cursorPos()
    for Current in range(NUMBER):
        #x1,y1 = cursorPos()
        #move(x,y)
        percent = ceil((Current+1)*100/NUMBER)
        Char = floor(percent/2)
        String = preffix+f"\033[97m[\033[94m{chr(9632)*Char:<50}\033[97m]\033[93m {percent:>3}%\033[0m ({Current+1}/{NUMBER})"+suffix
        sys.stdout.write(String+"\r");sys.stdout.flush()
        #move(x1,y1)
        yield Current

class ProgressBar(object):
    CHAR_ON  = '='
    CHAR_OFF = ' '

    def __init__(self, end=100, length=65):
        self._end = end
        self._length = length
        self._chars = None
        self._value = 0

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = max(0, min(value, self._end))
        if self._chars != (c := int(self._length * (self._value / self._end))):
            self._chars = c
            sys.stdout.write("\r  {:3n}% [{}{}]".format(
                int((self._value / self._end) * 100.0),
                self.CHAR_ON  * int(self._chars),
                self.CHAR_OFF * int(self._length - self._chars),
            ))
            sys.stdout.flush()

    def __enter__(self):
        self.value = 0
        return self

    def __exit__(self, *args, **kwargs):
        sys.stdout.write('\n')

if __name__ == "__main__":
    for n in Progress_Bar(100,"\033[92mProgress\033[0m\t:"):
        for x in range(2, ceil(n**(1/2))):
            if n % x == 0:
                break
        else:
            #print(n,end="",flush=True)
            pass
    print()

    count = 150
    print("starting things:")

    with ProgressBar(count) as bar:
        for n in range(count + 1):
            bar.value += 1
            time.sleep(0.01)

    print("done")
import subprocess
import datetime
import sys
import re

week_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']

built_in_pattern = re.compile('[0-9]+ Built-in Output')
number_pattern = re.compile('[0-9]+')


def se_puede_hablar():
    now = datetime.datetime.now().time()
    today = datetime.date.today()

    if today.strftime("%A") in week_day and datetime.time(18) < now < datetime.time(23):
        return True
    if today.strftime("%A") in weekend and datetime.time(11) < now < datetime.time(23):
        return True
    return False


def say(sentence):
    if sys.platform == "darwin":
        # only if we are in a Mac
        if se_puede_hablar():
            # asks for output devices
            say_output = subprocess.check_output(["say", "-a", "?"])
            for line in say_output.split("\n"):
                if built_in_pattern.search(line):
                    numero = number_pattern.search(line)
                    if numero:
                        subprocess.call(["say", "-a", numero.group(0), sentence])
                        break

            return
    print "say: ", sentence


if __name__ == "__main__":
    """
    we test if all is working properly
    """
    say('hola')
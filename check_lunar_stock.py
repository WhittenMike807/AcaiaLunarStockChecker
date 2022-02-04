import requests
from packages.lunar_data import *
from termcolor import *
from datetime import datetime
from time import *
from beepy import beep
from reprint import output
import schedule
import math
import webbrowser

def pl(number, unit):
    return f'{number} {unit}s' if number > 1 or isinstance(number, float) else f'{number} {unit}'

def generateTimerText(hours, mins, secs):
    startingText = 'Will Start Checking in'
    
    secText = pl(secs, 'Second')
    hourText = pl(hours, 'Hour')
    minText = pl(mins, 'Minute')
    
    if hours == 0 and mins == 0:
        return f'{startingText} {secText}'
    elif hours == 0 and mins != 0:
        return f'{startingText} {minText} and {secText}'
    else:
        return f'{startingText} {hourText} {minText} and {secText}'

def countdown(t):
    with output(initial_len=1, interval=0) as output_lines:
        while t:
            hours, remainder = divmod(t, 3600)
            mins, secs = divmod(remainder, 60)
            output_lines[0] = generateTimerText(hours, mins, secs)
            sleep(1)
            t -= 1
        output_lines[0] = 'Starting Process Now!!'
        beep(sound=4)
        output_lines.clear()
    schedule.run_pending()

def getLunar2021Data():
    try:
        response = requests.get('https://acaia.co/products/lunar_2021.js')
        response.raise_for_status()
        returnJson = response.json()
        return returnJson
    except requests.exceptions.RequestException as err:
        print(err)    

def printAvailabilityStatus(_lunarVariant:Variant):
    _acaiaBlackLunarURL = 'https://acaia.co/collections/coffee-scales/products/lunar_2021?variant=41056516178098'
    _acaiaWhiteLunarURL = 'https://acaia.co/collections/coffee-scales/products/lunar_2021?variant=41056516210866'
    
    productName = _lunarVariant.name
    
    startingText = f'{productName} Is Currently'
    statusText, textColor = ("Available", "green") if _lunarVariant.available else ("Unavailable", "red")
    
    if _lunarVariant.available:
        beep(sound=6)
    
    if _lunarVariant.available and _lunarVariant.name == 'Lunar 2021 - Black':
        webbrowser.open(_acaiaBlackLunarURL)
    
    if _lunarVariant.available and _lunarVariant.name == 'Lunar 2021 - Silver':
        webbrowser.open(_acaiaWhiteLunarURL)
    
    return f'{startingText} {colored(statusText, textColor, attrs=["bold"])}'
    

def job(condition):
    with output(initial_len=3, interval=0) as output_lines:
        while condition == True:
            now = datetime.now()
            currentTimeText = now.strftime('%#I:%M:%S %p').lstrip("0").replace(" 0", " ")
            output_lines[0] = f'Last Checked At: {currentTimeText}'
            
            _lunar2021Data = getLunar2021Data()
            _lunar2021DataDict = lunar_from_dict(_lunar2021Data)
            _lunarVariants = _lunar2021DataDict.variants
            
            output_lines[1] = printAvailabilityStatus(_lunarVariants[0])
            output_lines[2] = printAvailabilityStatus(_lunarVariants[1])
            
            sleep(10)

schedule.every().day.at("11:57:55").do(job, condition=True)


while True:
    n = schedule.idle_seconds()
    if n is None:
        break
    elif n > 0:
        countdown(int(math.ceil(n)))
from datetime import datetime, time

def get_hours():
    return str(datetime.now().time().hour)


def get_optimize_min():
    if len(str(datetime.now().time().minute)) == 1:
        minu = '0' + str(datetime.now().time().minute)
    else:
        minu = str(datetime.now().time().minute)
        
    return minu


def get_current_time():
    minu = get_optimize_min()
    hour = get_hours()
    return f'{hour}:{minu}'
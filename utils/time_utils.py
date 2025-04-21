from datetime import datetime, time
import pytz

# Часовой пояс Москвы
MOSCOW_TZ = pytz.timezone("Europe/Moscow")

def get_hours():
    now = datetime.now(MOSCOW_TZ)
    return str(now.hour)

def get_optimize_min():
    now = datetime.now(MOSCOW_TZ)
    minute = now.minute
    return f"{minute:02d}"  # автоматически добавит ведущий 0

def get_current_time():
    hour = get_hours()
    minute = get_optimize_min()
    return f"{hour}:{minute}"
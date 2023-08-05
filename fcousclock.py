import time
import datetime

def focus_clock(minutes):
    end_time = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
    while datetime.datetime.now() < end_time:
        remaining_time = end_time - datetime.datetime.now()
        remaining_seconds = remaining_time.total_seconds()
        minutes = int(remaining_seconds // 60)
        seconds = int(remaining_seconds % 60)
        time_left = f"{minutes:02d}:{seconds:02d}"
        print(f"Remaining Time: {time_left}", end="\r")
        time.sleep(1)
    print("Time's up! Focus session completed.")

focus_clock(25)  # 设置专注时长，这里是25分钟

import time
import schedule
from plyer import notification

# function to trigger notification
def send_break_alert(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )

# helper functions for the jobs
def hydration_alert():
    send_break_alert("Hydration Alert", "Drink some water!")

def posture_alert():
    send_break_alert("Posture Check", "Sit up straight and stretch!")

# scheduling tasks
schedule.every(10).seconds.do(hydration_alert)
schedule.every(20).seconds.do(posture_alert)
print("Reminder daemon is running... Press Ctrl+C to stop.")
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping reminder daemon. Goodbye!")
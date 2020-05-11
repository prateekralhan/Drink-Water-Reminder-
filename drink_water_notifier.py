import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title ="**Please Drink Water Now buddy!",
        message = "Health authorities commonly recommend eight 8-ounce glasses which is ~2 litres, or half a gallon. This is called the 8×8 rule !",
        #app_icon = "C:/Users/S93Z3S/Desktop/Res_Dev/Drink water notifier/glass.ico",
        timeout = 12
    )

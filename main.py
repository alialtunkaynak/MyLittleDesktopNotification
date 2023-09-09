import plyer
from plyer import notification

notification_title = " Merhaba Görüşmeyeli Uzun zaman oldu "
notification_message = " You Must Learn Artificial İntelligence & Machine Learning."
app_icon = "Notification.ico",

notification.notify(
    title = notification_title,
    message = notification_message,
    app_icon = None,
    timeout = 10,
    toast = False
)


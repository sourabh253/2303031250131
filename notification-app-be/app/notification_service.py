from app.database import notifications

def add_notification(notification):
    notifications.append(notification)

def get_notifications():
    return notifications
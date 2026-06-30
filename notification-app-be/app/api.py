from fastapi import APIRouter
from app.models import Notification
from app.notification_service import add_notification, get_notifications

router = APIRouter()

@router.post("/notifications")
def create_notification(notification: Notification):
    add_notification(notification)
    return {
        "message": "Notification Added"
    }

@router.get("/notifications")
def all_notifications():
    return get_notifications()
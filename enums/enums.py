from enum import Enum

class UserRole(str, Enum):
    STUNDENT = "student"
    TUTOR = "tutor"
    ADMIN = "admin"

class WeekDay(str, Enum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"
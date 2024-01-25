from enum import Enum


class Status(Enum):
    QUEUED='queued'
    IN_PROGRESS='in_progress'
    COMPLETED='completed'
    WAITING='waiting'
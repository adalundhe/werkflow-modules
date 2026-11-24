from __future__ import annotations
from pydantic import BaseModel
from .detective_date_filter import DetectiveDateFilter
from .detective_string_filter import DetectiveStringFilter


class DetectiveFilterCriteria(BaseModel):
    Severity: DetectiveStringFilter | None = None
    Status: DetectiveStringFilter | None = None
    State: DetectiveStringFilter | None = None
    EntityArn: DetectiveStringFilter | None = None
    CreatedTime: DetectiveDateFilter | None = None

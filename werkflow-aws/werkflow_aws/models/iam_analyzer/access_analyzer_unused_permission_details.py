from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .access_analyzer_unused_action import AccessAnalyzerUnusedAction


class AccessAnalyzerUnusedPermissionDetails(BaseModel):
    actions: list[AccessAnalyzerUnusedAction] | None = None
    serviceNamespace: StrictStr | None = None
    lastAccessed: datetime.datetime | StrictStr | None = None

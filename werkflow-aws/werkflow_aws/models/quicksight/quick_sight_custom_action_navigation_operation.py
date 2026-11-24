from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_local_navigation_configuration import QuickSightLocalNavigationConfiguration


class QuickSightCustomActionNavigationOperation(BaseModel):
    LocalNavigationConfiguration: QuickSightLocalNavigationConfiguration | None = None

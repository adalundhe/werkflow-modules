from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_resource_permission import QuickSightResourcePermission


class QuickSightLinkSharingConfiguration(BaseModel):
    Permissions: list[QuickSightResourcePermission] | None = None

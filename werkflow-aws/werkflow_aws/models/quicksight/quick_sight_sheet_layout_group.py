from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_sheet_layout_group_member import QuickSightSheetLayoutGroupMember


class QuickSightSheetLayoutGroup(BaseModel):
    Id: StrictStr | None = None
    Members: list[QuickSightSheetLayoutGroupMember] | None = None

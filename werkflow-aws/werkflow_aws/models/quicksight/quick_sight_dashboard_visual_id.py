from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDashboardVisualId(BaseModel):
    DashboardId: StrictStr
    SheetId: StrictStr
    VisualId: StrictStr

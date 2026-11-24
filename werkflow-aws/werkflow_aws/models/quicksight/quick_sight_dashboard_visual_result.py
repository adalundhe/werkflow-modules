from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDashboardVisualResult(BaseModel):
    DashboardId: StrictStr | None = None
    DashboardName: StrictStr | None = None
    SheetId: StrictStr | None = None
    SheetName: StrictStr | None = None
    VisualId: StrictStr | None = None
    VisualTitle: StrictStr | None = None
    VisualSubtitle: StrictStr | None = None
    DashboardUrl: StrictStr | None = None

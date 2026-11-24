from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_dashboard_source_template import QuickSightDashboardSourceTemplate


class QuickSightDashboardSourceEntity(BaseModel):
    SourceTemplate: QuickSightDashboardSourceTemplate | None = None

from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_cascading_control_source import QuickSightCascadingControlSource


class QuickSightCascadingControlConfiguration(BaseModel):
    SourceControls: list[QuickSightCascadingControlSource] | None = None

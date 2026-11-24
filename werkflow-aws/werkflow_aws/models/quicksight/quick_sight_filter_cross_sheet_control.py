from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_cascading_control_configuration import QuickSightCascadingControlConfiguration


class QuickSightFilterCrossSheetControl(BaseModel):
    FilterControlId: StrictStr | None = None
    SourceFilterId: StrictStr | None = None
    CascadingControlConfiguration: QuickSightCascadingControlConfiguration | None = None

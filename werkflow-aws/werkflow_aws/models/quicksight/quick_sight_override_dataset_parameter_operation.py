from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_new_default_values import QuickSightNewDefaultValues


class QuickSightOverrideDatasetParameterOperation(BaseModel):
    ParameterName: StrictStr | None = None
    NewParameterName: StrictStr | None = None
    NewDefaultValues: QuickSightNewDefaultValues | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightLabelActionMapping(BaseModel):
    LabelId: StrictStr | None = None
    LabelName: StrictStr | None = None
    Action: StrictStr | None = None

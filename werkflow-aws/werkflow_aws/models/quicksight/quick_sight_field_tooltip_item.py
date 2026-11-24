from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightFieldTooltipItem(BaseModel):
    FieldId: StrictStr | None = None
    Label: StrictStr | None = None
    Visibility: StrictStr | None = None
    TooltipTarget: StrictStr | None = None

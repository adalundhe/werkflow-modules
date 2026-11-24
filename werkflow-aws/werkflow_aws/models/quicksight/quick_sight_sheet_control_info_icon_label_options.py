from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSheetControlInfoIconLabelOptions(BaseModel):
    Visibility: StrictStr | None = None
    InfoIconText: StrictStr | None = None

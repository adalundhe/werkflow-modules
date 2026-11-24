from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDecalSettings(BaseModel):
    ElementValue: StrictStr | None = None
    DecalVisibility: StrictStr | None = None
    DecalColor: StrictStr | None = None
    DecalPatternType: StrictStr | None = None
    DecalStyleType: StrictStr | None = None

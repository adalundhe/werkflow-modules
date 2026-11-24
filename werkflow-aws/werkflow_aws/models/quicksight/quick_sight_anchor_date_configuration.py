from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAnchorDateConfiguration(BaseModel):
    AnchorOption: StrictStr | None = None
    ParameterName: StrictStr | None = None

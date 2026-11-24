from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightTopicSingularFilterConstant(BaseModel):
    ConstantType: StrictStr | None = None
    SingularConstant: StrictStr | None = None

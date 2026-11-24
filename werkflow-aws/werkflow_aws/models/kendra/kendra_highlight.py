from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class KendraHighlight(BaseModel):
    BeginOffset: StrictInt | None = None
    EndOffset: StrictInt | None = None
    TopAnswer: StrictBool | None = None
    Type: StrictStr | None = None

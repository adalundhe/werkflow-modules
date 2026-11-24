from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class WAFv2PreParseTextTransformation(BaseModel):
    Priority: StrictInt | None = None
    Type: StrictStr | None = None

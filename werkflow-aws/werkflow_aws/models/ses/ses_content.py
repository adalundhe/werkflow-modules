from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESContent(BaseModel):
    Data: StrictStr
    Charset: StrictStr | None = None

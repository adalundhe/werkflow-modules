from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectFontFamily(BaseModel):
    Default: StrictStr | None = None

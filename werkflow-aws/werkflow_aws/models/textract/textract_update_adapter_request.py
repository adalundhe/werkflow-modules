from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class TextractUpdateAdapterRequest(BaseModel):
    AdapterId: StrictStr
    Description: StrictStr | None = None
    AdapterName: StrictStr | None = None
    AutoUpdate: Literal['ENABLED', 'DISABLED'] | None = None

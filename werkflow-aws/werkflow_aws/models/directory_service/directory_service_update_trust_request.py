from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DirectoryServiceUpdateTrustRequest(BaseModel):
    TrustId: StrictStr
    SelectiveAuth: Literal['Enabled', 'Disabled'] | None = None

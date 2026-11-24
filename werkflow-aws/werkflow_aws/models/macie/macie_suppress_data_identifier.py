from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class MacieSuppressDataIdentifier(BaseModel):
    id: StrictStr | None = None
    type: Literal['CUSTOM', 'MANAGED'] | None = None

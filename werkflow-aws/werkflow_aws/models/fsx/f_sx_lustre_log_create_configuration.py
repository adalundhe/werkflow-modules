from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class FSxLustreLogCreateConfiguration(BaseModel):
    Level: Literal['DISABLED', 'WARN_ONLY', 'ERROR_ONLY', 'WARN_ERROR']
    Destination: StrictStr | None = None

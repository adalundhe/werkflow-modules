from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectPalettePrimary(BaseModel):
    Default: StrictStr | None = None
    Active: StrictStr | None = None
    ContrastText: StrictStr | None = None

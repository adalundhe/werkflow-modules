from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieIpCity(BaseModel):
    name: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxOpenZFSClientConfiguration(BaseModel):
    Clients: StrictStr | None = None
    Options: list[StrictStr] | None = None

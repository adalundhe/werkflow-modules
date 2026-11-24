from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystExecuteCommandSessionConfiguration(BaseModel):
    command: StrictStr
    arguments: list[StrictStr] | None = None

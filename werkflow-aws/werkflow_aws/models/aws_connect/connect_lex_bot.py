from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectLexBot(BaseModel):
    Name: StrictStr | None = None
    LexRegion: StrictStr | None = None

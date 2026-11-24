from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectLexV2Bot(BaseModel):
    AliasArn: StrictStr | None = None

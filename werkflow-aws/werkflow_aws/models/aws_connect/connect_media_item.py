from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectMediaItem(BaseModel):
    Type: StrictStr | None = None
    Source: StrictStr | None = None

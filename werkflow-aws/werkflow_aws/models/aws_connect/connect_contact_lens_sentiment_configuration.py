from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectContactLensSentimentConfiguration(BaseModel):
    Behavior: StrictStr | None = None

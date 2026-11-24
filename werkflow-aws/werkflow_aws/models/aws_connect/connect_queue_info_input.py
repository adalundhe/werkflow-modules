from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectQueueInfoInput(BaseModel):
    Id: StrictStr | None = None

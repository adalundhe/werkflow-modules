from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ConnectVoicemailInfo(BaseModel):
    NumberOfVoicemails: StrictInt | None = None

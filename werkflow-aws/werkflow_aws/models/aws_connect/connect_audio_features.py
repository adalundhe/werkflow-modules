from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAudioFeatures(BaseModel):
    EchoReduction: StrictStr | None = None

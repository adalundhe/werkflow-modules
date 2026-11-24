from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectMediaPlacement(BaseModel):
    AudioHostUrl: StrictStr | None = None
    AudioFallbackUrl: StrictStr | None = None
    SignalingUrl: StrictStr | None = None
    TurnControlUrl: StrictStr | None = None
    EventIngestionUrl: StrictStr | None = None

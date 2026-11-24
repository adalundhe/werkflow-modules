from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectVoiceCallEntryPointParameters(BaseModel):
    SourcePhoneNumber: StrictStr | None = None
    DestinationPhoneNumber: StrictStr | None = None
    FlowId: StrictStr | None = None

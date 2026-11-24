from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectSuspendContactRecordingRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    InitialContactId: StrictStr
    ContactRecordingType: Literal['AGENT', 'IVR', 'SCREEN'] | None = None

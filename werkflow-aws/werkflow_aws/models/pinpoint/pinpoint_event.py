from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .pinpoint_session import PinpointSession


class PinpointEvent(BaseModel):
    EventType: StrictStr
    Timestamp: StrictStr
    AppPackageName: StrictStr | None = None
    AppTitle: StrictStr | None = None
    AppVersionCode: StrictStr | None = None
    Attributes: dict[StrictStr, StrictStr] | None = None
    ClientSdkVersion: StrictStr | None = None
    Metrics: dict[StrictStr, StrictFloat | StrictInt] | None = None
    SdkName: StrictStr | None = None
    Session: PinpointSession | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DMSSupportedEndpointType(BaseModel):
    EngineName: StrictStr | None = None
    SupportsCDC: StrictBool | None = None
    EndpointType: StrictStr | None = None
    ReplicationInstanceEngineMinimumVersion: StrictStr | None = None
    EngineDisplayName: StrictStr | None = None

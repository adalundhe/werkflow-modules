from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FSxWindowsFsrmConfiguration(BaseModel):
    FsrmServiceEnabled: StrictBool | None = None
    EventLogDestination: StrictStr | None = None

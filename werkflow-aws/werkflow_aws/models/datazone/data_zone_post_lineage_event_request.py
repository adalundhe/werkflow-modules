from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class DataZonePostLineageEventRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    domainIdentifier: StrictStr
    event: StrictBytes | BinaryIO | StrictStr
    clientToken: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseHttpEndpointConfiguration(BaseModel):
    Url: StrictStr
    Name: StrictStr | None = None
    AccessKey: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseHttpEndpointDescription(BaseModel):
    Url: StrictStr | None = None
    Name: StrictStr | None = None

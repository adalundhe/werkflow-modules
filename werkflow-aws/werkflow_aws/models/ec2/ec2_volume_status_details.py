from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2VolumeStatusDetails(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None

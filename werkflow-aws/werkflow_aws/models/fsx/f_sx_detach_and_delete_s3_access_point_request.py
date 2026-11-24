from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxDetachAndDeleteS3AccessPointRequest(BaseModel):
    Name: StrictStr
    ClientRequestToken: StrictStr | None = None

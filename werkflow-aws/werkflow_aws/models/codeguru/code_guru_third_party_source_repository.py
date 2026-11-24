from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeGuruThirdPartySourceRepository(BaseModel):
    Name: StrictStr
    ConnectionArn: StrictStr
    Owner: StrictStr

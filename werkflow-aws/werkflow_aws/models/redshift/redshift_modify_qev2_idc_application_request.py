from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftModifyQev2IdcApplicationRequest(BaseModel):
    Qev2IdcApplicationArn: StrictStr
    IdcDisplayName: StrictStr | None = None

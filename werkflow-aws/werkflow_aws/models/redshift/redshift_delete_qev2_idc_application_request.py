from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeleteQev2IdcApplicationRequest(BaseModel):
    Qev2IdcApplicationArn: StrictStr

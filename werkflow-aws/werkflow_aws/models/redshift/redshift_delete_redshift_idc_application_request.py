from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeleteRedshiftIdcApplicationRequest(BaseModel):
    RedshiftIdcApplicationArn: StrictStr

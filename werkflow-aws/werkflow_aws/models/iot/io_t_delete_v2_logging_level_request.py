from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class IoTDeleteV2LoggingLevelRequest(BaseModel):
    targetType: Literal['DEFAULT', 'THING_GROUP', 'CLIENT_ID', 'SOURCE_IP', 'PRINCIPAL_ID']
    targetName: StrictStr

from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListV2LoggingLevelsRequest(BaseModel):
    targetType: Literal['DEFAULT', 'THING_GROUP', 'CLIENT_ID', 'SOURCE_IP', 'PRINCIPAL_ID'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None

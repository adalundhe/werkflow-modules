from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListPrincipalThingsV2Request(BaseModel):
    principal: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    thingPrincipalType: Literal['EXCLUSIVE_THING', 'NON_EXCLUSIVE_THING'] | None = None

from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class IoTAttachThingPrincipalRequest(BaseModel):
    thingName: StrictStr
    principal: StrictStr
    thingPrincipalType: Literal['EXCLUSIVE_THING', 'NON_EXCLUSIVE_THING'] | None = None

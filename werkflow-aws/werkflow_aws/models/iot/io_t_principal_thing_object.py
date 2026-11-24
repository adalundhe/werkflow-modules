from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTPrincipalThingObject(BaseModel):
    thingName: StrictStr | None = None
    thingPrincipalType: StrictStr | None = None

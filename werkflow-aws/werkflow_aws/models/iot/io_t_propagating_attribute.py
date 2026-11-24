from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTPropagatingAttribute(BaseModel):
    userPropertyKey: StrictStr | None = None
    thingAttribute: StrictStr | None = None
    connectionAttribute: StrictStr | None = None

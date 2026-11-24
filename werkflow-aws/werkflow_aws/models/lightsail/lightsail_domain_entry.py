from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailDomainEntry(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    target: StrictStr | None = None
    isAlias: StrictBool | None = None
    type: StrictStr | None = None
    options: dict[StrictStr, StrictStr] | None = None

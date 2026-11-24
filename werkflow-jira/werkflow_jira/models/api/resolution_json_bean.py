from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ResolutionJsonBean(BaseModel):
    default: StrictBool | None = None
    description: StrictStr | None = None
    iconUrl: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    self: StrictStr | None = None

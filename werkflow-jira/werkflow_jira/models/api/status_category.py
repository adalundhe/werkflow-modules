from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr


class StatusCategory(BaseModel):
    model_config = ConfigDict(extra="allow")

    colorName: StrictStr | None = None
    id: StrictInt | None = None
    key: StrictStr | None = None
    name: StrictStr | None = None
    self: StrictStr | None = None

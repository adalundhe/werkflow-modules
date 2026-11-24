from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class PriorityWithSequence(BaseModel):
    description: StrictStr | None = None
    iconUrl: StrictStr | None = None
    id: StrictStr | None = None
    isDefault: StrictBool | None = None
    name: StrictStr | None = None
    self: StrictStr | None = None
    sequence: StrictStr | None = None
    statusColor: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ApplicationProperty(BaseModel):
    allowedValues: list[StrictStr] | None = None
    defaultValue: StrictStr | None = None
    desc: StrictStr | None = None
    example: StrictStr | None = None
    id: StrictStr | None = None
    key: StrictStr | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None
    value: StrictStr | None = None

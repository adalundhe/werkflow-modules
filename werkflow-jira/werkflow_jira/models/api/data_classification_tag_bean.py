from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DataClassificationTagBean(BaseModel):
    color: StrictStr | None = None
    description: StrictStr | None = None
    guideline: StrictStr | None = None
    guidelineADF: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    rank: StrictInt | None = None
    status: StrictStr | None = None

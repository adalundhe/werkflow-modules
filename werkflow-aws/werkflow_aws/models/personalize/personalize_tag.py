from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeTag(BaseModel):
    tagKey: StrictStr | None = None
    tagValue: StrictStr | None = None

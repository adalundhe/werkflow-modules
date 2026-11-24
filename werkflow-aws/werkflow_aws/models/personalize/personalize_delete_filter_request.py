from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDeleteFilterRequest(BaseModel):
    filterArn: StrictStr

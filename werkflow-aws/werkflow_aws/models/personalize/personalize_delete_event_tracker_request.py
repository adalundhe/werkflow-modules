from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDeleteEventTrackerRequest(BaseModel):
    eventTrackerArn: StrictStr

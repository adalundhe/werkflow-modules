from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDescribeEventTrackerRequest(BaseModel):
    eventTrackerArn: StrictStr

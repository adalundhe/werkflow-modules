from __future__ import annotations
from pydantic import BaseModel, StrictBool


class CloudFormationEventFilter(BaseModel):
    FailedEvents: StrictBool | None = None

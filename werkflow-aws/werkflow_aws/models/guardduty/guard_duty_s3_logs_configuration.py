from __future__ import annotations
from pydantic import BaseModel, StrictBool


class GuardDutyS3LogsConfiguration(BaseModel):
    Enable: StrictBool

from __future__ import annotations
from pydantic import BaseModel, StrictBool


class GuardDutyScanEc2InstanceWithFindings(BaseModel):
    EbsVolumes: StrictBool | None = None

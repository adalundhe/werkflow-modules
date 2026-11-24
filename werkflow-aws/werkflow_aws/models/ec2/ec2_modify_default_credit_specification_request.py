from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyDefaultCreditSpecificationRequest(BaseModel):
    InstanceFamily: Literal['t2', 't3', 't3a', 't4g', 't8i', 't9g']
    CpuCredits: StrictStr
    DryRun: StrictBool | None = None

from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool


class ComputeOptimizerUpdateEnrollmentStatusRequest(BaseModel):
    status: Literal['Active', 'Inactive', 'Pending', 'Failed']
    includeMemberAccounts: StrictBool | None = None

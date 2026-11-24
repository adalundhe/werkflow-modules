from __future__ import annotations
from pydantic import BaseModel, StrictBool


class CloudFormationManagedExecution(BaseModel):
    Active: StrictBool | None = None

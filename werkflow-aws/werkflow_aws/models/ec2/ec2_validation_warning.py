from __future__ import annotations
from pydantic import BaseModel
from .ec2_validation_error import EC2ValidationError


class EC2ValidationWarning(BaseModel):
    Errors: list[EC2ValidationError] | None = None

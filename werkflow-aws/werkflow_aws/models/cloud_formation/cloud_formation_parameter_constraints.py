from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationParameterConstraints(BaseModel):
    AllowedValues: list[StrictStr] | None = None

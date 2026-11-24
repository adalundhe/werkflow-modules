from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFormationParameter(BaseModel):
    ParameterKey: StrictStr | None = None
    ParameterValue: StrictStr | None = None
    UsePreviousValue: StrictBool | None = None
    ResolvedValue: StrictStr | None = None

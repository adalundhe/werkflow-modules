from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFormationWarningProperty(BaseModel):
    PropertyPath: StrictStr | None = None
    Required: StrictBool | None = None
    Description: StrictStr | None = None

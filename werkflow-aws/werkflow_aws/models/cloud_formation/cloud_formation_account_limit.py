from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFormationAccountLimit(BaseModel):
    Name: StrictStr | None = None
    Value: StrictInt | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationRollbackTrigger(BaseModel):
    Arn: StrictStr | None = None
    Type: StrictStr | None = None

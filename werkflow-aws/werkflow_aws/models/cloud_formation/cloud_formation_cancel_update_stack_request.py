from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationCancelUpdateStackRequest(BaseModel):
    StackName: StrictStr
    ClientRequestToken: StrictStr | None = None

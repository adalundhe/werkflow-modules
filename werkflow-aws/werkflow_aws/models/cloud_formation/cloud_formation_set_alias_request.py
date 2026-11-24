from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationSetAliasRequest(BaseModel):
    StackName: StrictStr
    AliasName: StrictStr

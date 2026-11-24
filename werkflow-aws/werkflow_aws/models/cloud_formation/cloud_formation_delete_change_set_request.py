from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationDeleteChangeSetRequest(BaseModel):
    ChangeSetName: StrictStr
    StackName: StrictStr | None = None

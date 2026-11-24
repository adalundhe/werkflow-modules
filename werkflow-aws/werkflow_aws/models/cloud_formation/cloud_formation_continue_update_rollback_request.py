from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFormationContinueUpdateRollbackRequest(BaseModel):
    StackName: StrictStr
    RoleARN: StrictStr | None = None
    ResourcesToSkip: list[StrictStr] | None = None
    ClientRequestToken: StrictStr | None = None
    ForceRollback: StrictBool | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFormationExecuteChangeSetRequest(BaseModel):
    ChangeSetName: StrictStr
    StackName: StrictStr | None = None
    ClientRequestToken: StrictStr | None = None
    DisableRollback: StrictBool | None = None
    RetainExceptOnCreate: StrictBool | None = None

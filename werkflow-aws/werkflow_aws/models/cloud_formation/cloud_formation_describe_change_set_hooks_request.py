from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationDescribeChangeSetHooksRequest(BaseModel):
    ChangeSetName: StrictStr
    StackName: StrictStr | None = None
    NextToken: StrictStr | None = None
    LogicalResourceId: StrictStr | None = None

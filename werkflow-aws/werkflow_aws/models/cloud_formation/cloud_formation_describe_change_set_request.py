from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFormationDescribeChangeSetRequest(BaseModel):
    ChangeSetName: StrictStr
    StackName: StrictStr | None = None
    NextToken: StrictStr | None = None
    IncludePropertyValues: StrictBool | None = None

from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFormationChangeSetSummary(BaseModel):
    StackId: StrictStr | None = None
    StackName: StrictStr | None = None
    ChangeSetId: StrictStr | None = None
    ChangeSetName: StrictStr | None = None
    ExecutionStatus: StrictStr | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    IncludeNestedStacks: StrictBool | None = None
    ParentChangeSetId: StrictStr | None = None
    RootChangeSetId: StrictStr | None = None
    ImportExistingResources: StrictBool | None = None

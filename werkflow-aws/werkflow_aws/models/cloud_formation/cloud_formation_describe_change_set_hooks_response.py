from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_change_set_hook import CloudFormationChangeSetHook


class CloudFormationDescribeChangeSetHooksResponse(BaseModel):
    ChangeSetId: StrictStr | None = None
    ChangeSetName: StrictStr | None = None
    Hooks: list[CloudFormationChangeSetHook] | None = None
    Status: StrictStr | None = None
    NextToken: StrictStr | None = None
    StackId: StrictStr | None = None
    StackName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

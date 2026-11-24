from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFormationListHookResultsRequest(BaseModel):
    TargetType: Literal['CHANGE_SET', 'STACK', 'RESOURCE', 'CLOUD_CONTROL'] | None = None
    TargetId: StrictStr | None = None
    TypeArn: StrictStr | None = None
    Status: Literal['HOOK_IN_PROGRESS', 'HOOK_COMPLETE_SUCCEEDED', 'HOOK_COMPLETE_FAILED', 'HOOK_FAILED'] | None = None
    NextToken: StrictStr | None = None

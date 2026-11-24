from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_hook_result_summary import CloudFormationHookResultSummary


class CloudFormationListHookResultsResponse(BaseModel):
    TargetType: StrictStr | None = None
    TargetId: StrictStr | None = None
    HookResults: list[CloudFormationHookResultSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

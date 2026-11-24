from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_stack_refactor_action import CloudFormationStackRefactorAction


class CloudFormationListStackRefactorActionsResponse(BaseModel):
    StackRefactorActions: list[CloudFormationStackRefactorAction] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

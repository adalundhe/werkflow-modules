from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cloud_formation_stack_set_operation_preferences import CloudFormationStackSetOperationPreferences


class CloudFormationDetectStackSetDriftRequest(BaseModel):
    StackSetName: StrictStr
    OperationPreferences: CloudFormationStackSetOperationPreferences | None = None
    OperationId: StrictStr | None = None
    CallAs: Literal['SELF', 'DELEGATED_ADMIN'] | None = None

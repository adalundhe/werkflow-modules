from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cloud_formation_stack_set_operation_preferences import CloudFormationStackSetOperationPreferences


class CloudFormationImportStacksToStackSetRequest(BaseModel):
    StackSetName: StrictStr
    StackIds: list[StrictStr] | None = None
    StackIdsUrl: StrictStr | None = None
    OrganizationalUnitIds: list[StrictStr] | None = None
    OperationPreferences: CloudFormationStackSetOperationPreferences | None = None
    OperationId: StrictStr | None = None
    CallAs: Literal['SELF', 'DELEGATED_ADMIN'] | None = None

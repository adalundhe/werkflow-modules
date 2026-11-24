from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_formation_deployment_targets import CloudFormationDeploymentTargets
from .cloud_formation_stack_set_operation_preferences import CloudFormationStackSetOperationPreferences


class CloudFormationDeleteStackInstancesRequest(BaseModel):
    StackSetName: StrictStr
    Regions: list[StrictStr]
    RetainStacks: StrictBool
    Accounts: list[StrictStr] | None = None
    DeploymentTargets: CloudFormationDeploymentTargets | None = None
    OperationPreferences: CloudFormationStackSetOperationPreferences | None = None
    OperationId: StrictStr | None = None
    CallAs: Literal['SELF', 'DELEGATED_ADMIN'] | None = None

from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cloud_formation_deployment_targets import CloudFormationDeploymentTargets
from .cloud_formation_parameter import CloudFormationParameter
from .cloud_formation_stack_set_operation_preferences import CloudFormationStackSetOperationPreferences


class CloudFormationUpdateStackInstancesRequest(BaseModel):
    StackSetName: StrictStr
    Regions: list[StrictStr]
    Accounts: list[StrictStr] | None = None
    DeploymentTargets: CloudFormationDeploymentTargets | None = None
    ParameterOverrides: list[CloudFormationParameter] | None = None
    OperationPreferences: CloudFormationStackSetOperationPreferences | None = None
    OperationId: StrictStr | None = None
    CallAs: Literal['SELF', 'DELEGATED_ADMIN'] | None = None

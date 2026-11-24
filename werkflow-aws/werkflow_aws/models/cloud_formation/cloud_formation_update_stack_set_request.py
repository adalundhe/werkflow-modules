from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_formation_auto_deployment import CloudFormationAutoDeployment
from .cloud_formation_deployment_targets import CloudFormationDeploymentTargets
from .cloud_formation_managed_execution import CloudFormationManagedExecution
from .cloud_formation_parameter import CloudFormationParameter
from .cloud_formation_stack_set_operation_preferences import CloudFormationStackSetOperationPreferences
from .cloud_formation_tag import CloudFormationTag


class CloudFormationUpdateStackSetRequest(BaseModel):
    StackSetName: StrictStr
    Description: StrictStr | None = None
    TemplateBody: StrictStr | None = None
    TemplateURL: StrictStr | None = None
    UsePreviousTemplate: StrictBool | None = None
    Parameters: list[CloudFormationParameter] | None = None
    Capabilities: list[Literal['CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM', 'CAPABILITY_AUTO_EXPAND']] | None = None
    Tags: list[CloudFormationTag] | None = None
    OperationPreferences: CloudFormationStackSetOperationPreferences | None = None
    AdministrationRoleARN: StrictStr | None = None
    ExecutionRoleName: StrictStr | None = None
    DeploymentTargets: CloudFormationDeploymentTargets | None = None
    PermissionModel: Literal['SERVICE_MANAGED', 'SELF_MANAGED'] | None = None
    AutoDeployment: CloudFormationAutoDeployment | None = None
    OperationId: StrictStr | None = None
    Accounts: list[StrictStr] | None = None
    Regions: list[StrictStr] | None = None
    CallAs: Literal['SELF', 'DELEGATED_ADMIN'] | None = None
    ManagedExecution: CloudFormationManagedExecution | None = None
    ExecutionRoleTemplateBody: StrictStr | None = None
    ExecutionRoleTemplateUrl: StrictStr | None = None
    UseAdminExecutionRole: StrictBool | None = None
    StackSetOutputBucket: StrictStr | None = None

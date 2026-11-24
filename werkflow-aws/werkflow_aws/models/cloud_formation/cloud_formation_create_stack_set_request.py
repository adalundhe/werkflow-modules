from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cloud_formation_auto_deployment import CloudFormationAutoDeployment
from .cloud_formation_managed_execution import CloudFormationManagedExecution
from .cloud_formation_parameter import CloudFormationParameter
from .cloud_formation_tag import CloudFormationTag


class CloudFormationCreateStackSetRequest(BaseModel):
    StackSetName: StrictStr
    Description: StrictStr | None = None
    TemplateBody: StrictStr | None = None
    TemplateURL: StrictStr | None = None
    StackId: StrictStr | None = None
    Parameters: list[CloudFormationParameter] | None = None
    Capabilities: list[Literal['CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM', 'CAPABILITY_AUTO_EXPAND']] | None = None
    Tags: list[CloudFormationTag] | None = None
    AdministrationRoleARN: StrictStr | None = None
    ExecutionRoleName: StrictStr | None = None
    PermissionModel: Literal['SERVICE_MANAGED', 'SELF_MANAGED'] | None = None
    AutoDeployment: CloudFormationAutoDeployment | None = None
    CallAs: Literal['SELF', 'DELEGATED_ADMIN'] | None = None
    ClientRequestToken: StrictStr | None = None
    ManagedExecution: CloudFormationManagedExecution | None = None
    ExecutionRoleTemplateBody: StrictStr | None = None
    ExecutionRoleTemplateUrl: StrictStr | None = None
    StackSetOutputBucket: StrictStr | None = None

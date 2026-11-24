from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_formation_deployment_config import CloudFormationDeploymentConfig
from .cloud_formation_parameter import CloudFormationParameter
from .cloud_formation_rollback_configuration import CloudFormationRollbackConfiguration
from .cloud_formation_tag import CloudFormationTag


class CloudFormationUpdateStackRequest(BaseModel):
    StackName: StrictStr
    TemplateBody: StrictStr | None = None
    TemplateURL: StrictStr | None = None
    UsePreviousTemplate: StrictBool | None = None
    StackPolicyDuringUpdateBody: StrictStr | None = None
    StackPolicyDuringUpdateURL: StrictStr | None = None
    Parameters: list[CloudFormationParameter] | None = None
    Capabilities: list[Literal['CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM', 'CAPABILITY_AUTO_EXPAND']] | None = None
    ResourceTypes: list[StrictStr] | None = None
    RoleARN: StrictStr | None = None
    RollbackConfiguration: CloudFormationRollbackConfiguration | None = None
    StackPolicyBody: StrictStr | None = None
    StackPolicyURL: StrictStr | None = None
    NotificationARNs: list[StrictStr] | None = None
    Tags: list[CloudFormationTag] | None = None
    DisableRollback: StrictBool | None = None
    ClientRequestToken: StrictStr | None = None
    RetainExceptOnCreate: StrictBool | None = None
    DeploymentConfig: CloudFormationDeploymentConfig | None = None
    DisableValidation: StrictBool | None = None

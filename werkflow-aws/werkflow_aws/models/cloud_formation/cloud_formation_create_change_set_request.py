from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_formation_deployment_config import CloudFormationDeploymentConfig
from .cloud_formation_parameter import CloudFormationParameter
from .cloud_formation_resource_to_import import CloudFormationResourceToImport
from .cloud_formation_rollback_configuration import CloudFormationRollbackConfiguration
from .cloud_formation_tag import CloudFormationTag


class CloudFormationCreateChangeSetRequest(BaseModel):
    StackName: StrictStr
    ChangeSetName: StrictStr
    TemplateBody: StrictStr | None = None
    TemplateURL: StrictStr | None = None
    UsePreviousTemplate: StrictBool | None = None
    Parameters: list[CloudFormationParameter] | None = None
    Capabilities: list[Literal['CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM', 'CAPABILITY_AUTO_EXPAND']] | None = None
    ResourceTypes: list[StrictStr] | None = None
    RoleARN: StrictStr | None = None
    RollbackConfiguration: CloudFormationRollbackConfiguration | None = None
    NotificationARNs: list[StrictStr] | None = None
    Tags: list[CloudFormationTag] | None = None
    ClientToken: StrictStr | None = None
    Description: StrictStr | None = None
    ChangeSetType: Literal['CREATE', 'UPDATE', 'IMPORT'] | None = None
    ResourcesToImport: list[CloudFormationResourceToImport] | None = None
    IncludeNestedStacks: StrictBool | None = None
    OnStackFailure: Literal['DO_NOTHING', 'ROLLBACK', 'DELETE'] | None = None
    ImportExistingResources: StrictBool | None = None
    DeploymentMode: Literal['REVERT_DRIFT'] | None = None
    DeploymentConfig: CloudFormationDeploymentConfig | None = None
    DisableValidation: StrictBool | None = None

from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_formation_change import CloudFormationChange
from .cloud_formation_deployment_config import CloudFormationDeploymentConfig
from .cloud_formation_parameter import CloudFormationParameter
from .cloud_formation_rollback_configuration import CloudFormationRollbackConfiguration
from .cloud_formation_tag import CloudFormationTag


class CloudFormationDescribeChangeSetResponse(BaseModel):
    ChangeSetName: StrictStr | None = None
    ChangeSetId: StrictStr | None = None
    StackId: StrictStr | None = None
    StackName: StrictStr | None = None
    Description: StrictStr | None = None
    Parameters: list[CloudFormationParameter] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ExecutionStatus: StrictStr | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    StackDriftStatus: StrictStr | None = None
    NotificationARNs: list[StrictStr] | None = None
    RollbackConfiguration: CloudFormationRollbackConfiguration | None = None
    Capabilities: list[StrictStr] | None = None
    Tags: list[CloudFormationTag] | None = None
    Changes: list[CloudFormationChange] | None = None
    NextToken: StrictStr | None = None
    IncludeNestedStacks: StrictBool | None = None
    ParentChangeSetId: StrictStr | None = None
    RootChangeSetId: StrictStr | None = None
    OnStackFailure: StrictStr | None = None
    ImportExistingResources: StrictBool | None = None
    DeploymentMode: StrictStr | None = None
    DeploymentConfig: CloudFormationDeploymentConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None

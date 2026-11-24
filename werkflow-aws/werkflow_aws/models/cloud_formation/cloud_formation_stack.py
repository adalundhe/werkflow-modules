from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_formation_deployment_config import CloudFormationDeploymentConfig
from .cloud_formation_operation_entry import CloudFormationOperationEntry
from .cloud_formation_output import CloudFormationOutput
from .cloud_formation_parameter import CloudFormationParameter
from .cloud_formation_rollback_configuration import CloudFormationRollbackConfiguration
from .cloud_formation_stack_drift_information import CloudFormationStackDriftInformation
from .cloud_formation_tag import CloudFormationTag


class CloudFormationStack(BaseModel):
    StackId: StrictStr | None = None
    StackName: StrictStr | None = None
    ChangeSetId: StrictStr | None = None
    Description: StrictStr | None = None
    Parameters: list[CloudFormationParameter] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    DeletionTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    RollbackConfiguration: CloudFormationRollbackConfiguration | None = None
    StackStatus: StrictStr | None = None
    StackStatusReason: StrictStr | None = None
    DisableRollback: StrictBool | None = None
    DeploymentConfig: CloudFormationDeploymentConfig | None = None
    NotificationARNs: list[StrictStr] | None = None
    TimeoutInMinutes: StrictInt | None = None
    Capabilities: list[StrictStr] | None = None
    Outputs: list[CloudFormationOutput] | None = None
    RoleARN: StrictStr | None = None
    Tags: list[CloudFormationTag] | None = None
    EnableTerminationProtection: StrictBool | None = None
    ParentId: StrictStr | None = None
    RootId: StrictStr | None = None
    DriftInformation: CloudFormationStackDriftInformation | None = None
    RetainExceptOnCreate: StrictBool | None = None
    DeletionMode: StrictStr | None = None
    DetailedStatus: StrictStr | None = None
    LastOperations: list[CloudFormationOperationEntry] | None = None
    AliasName: StrictStr | None = None

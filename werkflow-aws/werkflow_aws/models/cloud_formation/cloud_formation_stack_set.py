from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_formation_auto_deployment import CloudFormationAutoDeployment
from .cloud_formation_managed_execution import CloudFormationManagedExecution
from .cloud_formation_parameter import CloudFormationParameter
from .cloud_formation_stack_set_drift_detection_details import CloudFormationStackSetDriftDetectionDetails
from .cloud_formation_tag import CloudFormationTag


class CloudFormationStackSet(BaseModel):
    StackSetName: StrictStr | None = None
    StackSetId: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    TemplateBody: StrictStr | None = None
    Parameters: list[CloudFormationParameter] | None = None
    Capabilities: list[StrictStr] | None = None
    Tags: list[CloudFormationTag] | None = None
    StackSetARN: StrictStr | None = None
    AdministrationRoleARN: StrictStr | None = None
    ExecutionRoleName: StrictStr | None = None
    StackSetDriftDetectionDetails: CloudFormationStackSetDriftDetectionDetails | None = None
    AutoDeployment: CloudFormationAutoDeployment | None = None
    PermissionModel: StrictStr | None = None
    OrganizationalUnitIds: list[StrictStr] | None = None
    ManagedExecution: CloudFormationManagedExecution | None = None
    Regions: list[StrictStr] | None = None
    StackSetOutputBucketPath: StrictStr | None = None

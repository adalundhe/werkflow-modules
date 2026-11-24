from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_formation_deployment_targets import CloudFormationDeploymentTargets
from .cloud_formation_regional_status_detail import CloudFormationRegionalStatusDetail
from .cloud_formation_stack_set_drift_detection_details import CloudFormationStackSetDriftDetectionDetails
from .cloud_formation_stack_set_operation_preferences import CloudFormationStackSetOperationPreferences
from .cloud_formation_stack_set_operation_status_details import CloudFormationStackSetOperationStatusDetails


class CloudFormationStackSetOperation(BaseModel):
    OperationId: StrictStr | None = None
    StackSetId: StrictStr | None = None
    Action: StrictStr | None = None
    Status: StrictStr | None = None
    OperationPreferences: CloudFormationStackSetOperationPreferences | None = None
    RetainStacks: StrictBool | None = None
    AdministrationRoleARN: StrictStr | None = None
    ExecutionRoleName: StrictStr | None = None
    CreationTimestamp: datetime.datetime | StrictStr | None = None
    EndTimestamp: datetime.datetime | StrictStr | None = None
    DeploymentTargets: CloudFormationDeploymentTargets | None = None
    StackSetDriftDetectionDetails: CloudFormationStackSetDriftDetectionDetails | None = None
    StatusReason: StrictStr | None = None
    StatusDetails: CloudFormationStackSetOperationStatusDetails | None = None
    RegionalStatusDetails: dict[StrictStr, CloudFormationRegionalStatusDetail] | None = None

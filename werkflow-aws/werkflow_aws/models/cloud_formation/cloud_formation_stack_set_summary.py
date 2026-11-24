from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_formation_auto_deployment import CloudFormationAutoDeployment
from .cloud_formation_managed_execution import CloudFormationManagedExecution


class CloudFormationStackSetSummary(BaseModel):
    StackSetName: StrictStr | None = None
    StackSetId: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    AutoDeployment: CloudFormationAutoDeployment | None = None
    PermissionModel: StrictStr | None = None
    DriftStatus: StrictStr | None = None
    LastDriftCheckTimestamp: datetime.datetime | StrictStr | None = None
    ManagedExecution: CloudFormationManagedExecution | None = None

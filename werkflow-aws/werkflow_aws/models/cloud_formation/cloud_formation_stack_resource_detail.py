from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_formation_module_info import CloudFormationModuleInfo
from .cloud_formation_stack_resource_drift_information import CloudFormationStackResourceDriftInformation


class CloudFormationStackResourceDetail(BaseModel):
    StackName: StrictStr | None = None
    StackId: StrictStr | None = None
    LogicalResourceId: StrictStr | None = None
    PhysicalResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    LastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
    ResourceStatus: StrictStr | None = None
    ResourceStatusReason: StrictStr | None = None
    Description: StrictStr | None = None
    Metadata: StrictStr | None = None
    DriftInformation: CloudFormationStackResourceDriftInformation | None = None
    ModuleInfo: CloudFormationModuleInfo | None = None

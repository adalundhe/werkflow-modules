from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_formation_module_info import CloudFormationModuleInfo
from .cloud_formation_stack_resource_drift_information_summary import CloudFormationStackResourceDriftInformationSummary


class CloudFormationStackResourceSummary(BaseModel):
    LogicalResourceId: StrictStr | None = None
    PhysicalResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    LastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
    ResourceStatus: StrictStr | None = None
    ResourceStatusReason: StrictStr | None = None
    DriftInformation: CloudFormationStackResourceDriftInformationSummary | None = None
    ModuleInfo: CloudFormationModuleInfo | None = None

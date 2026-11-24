from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_formation_stack_instance_comprehensive_status import CloudFormationStackInstanceComprehensiveStatus


class CloudFormationStackInstanceSummary(BaseModel):
    StackSetId: StrictStr | None = None
    Region: StrictStr | None = None
    Account: StrictStr | None = None
    StackId: StrictStr | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    StackInstanceStatus: CloudFormationStackInstanceComprehensiveStatus | None = None
    OrganizationalUnitId: StrictStr | None = None
    DriftStatus: StrictStr | None = None
    LastDriftCheckTimestamp: datetime.datetime | StrictStr | None = None
    LastOperationId: StrictStr | None = None

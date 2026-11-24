from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_formation_parameter import CloudFormationParameter
from .cloud_formation_stack_instance_comprehensive_status import CloudFormationStackInstanceComprehensiveStatus


class CloudFormationStackInstance(BaseModel):
    StackSetId: StrictStr | None = None
    Region: StrictStr | None = None
    Account: StrictStr | None = None
    StackId: StrictStr | None = None
    ParameterOverrides: list[CloudFormationParameter] | None = None
    Status: StrictStr | None = None
    StackInstanceStatus: CloudFormationStackInstanceComprehensiveStatus | None = None
    StatusReason: StrictStr | None = None
    OrganizationalUnitId: StrictStr | None = None
    DriftStatus: StrictStr | None = None
    LastDriftCheckTimestamp: datetime.datetime | StrictStr | None = None
    LastOperationId: StrictStr | None = None

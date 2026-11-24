from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_formation_stack_set_operation_preferences import CloudFormationStackSetOperationPreferences
from .cloud_formation_stack_set_operation_status_details import CloudFormationStackSetOperationStatusDetails


class CloudFormationStackSetOperationSummary(BaseModel):
    OperationId: StrictStr | None = None
    Action: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTimestamp: datetime.datetime | StrictStr | None = None
    EndTimestamp: datetime.datetime | StrictStr | None = None
    StatusReason: StrictStr | None = None
    StatusDetails: CloudFormationStackSetOperationStatusDetails | None = None
    OperationPreferences: CloudFormationStackSetOperationPreferences | None = None

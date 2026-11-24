from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_formation_operation_entry import CloudFormationOperationEntry
from .cloud_formation_stack_drift_information_summary import CloudFormationStackDriftInformationSummary


class CloudFormationStackSummary(BaseModel):
    StackId: StrictStr | None = None
    StackName: StrictStr | None = None
    TemplateDescription: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    DeletionTime: datetime.datetime | StrictStr | None = None
    StackStatus: StrictStr | None = None
    StackStatusReason: StrictStr | None = None
    ParentId: StrictStr | None = None
    RootId: StrictStr | None = None
    DriftInformation: CloudFormationStackDriftInformationSummary | None = None
    LastOperations: list[CloudFormationOperationEntry] | None = None

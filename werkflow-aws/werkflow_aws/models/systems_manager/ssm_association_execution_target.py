from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ssm_output_source import SSMOutputSource


class SSMAssociationExecutionTarget(BaseModel):
    AssociationId: StrictStr | None = None
    AssociationVersion: StrictStr | None = None
    ExecutionId: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Status: StrictStr | None = None
    DetailedStatus: StrictStr | None = None
    LastExecutionDate: datetime.datetime | StrictStr | None = None
    OutputSource: SSMOutputSource | None = None

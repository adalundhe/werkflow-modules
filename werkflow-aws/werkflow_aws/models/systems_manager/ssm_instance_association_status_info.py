from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ssm_instance_association_output_url import SSMInstanceAssociationOutputUrl


class SSMInstanceAssociationStatusInfo(BaseModel):
    AssociationId: StrictStr | None = None
    Name: StrictStr | None = None
    DocumentVersion: StrictStr | None = None
    AssociationVersion: StrictStr | None = None
    InstanceId: StrictStr | None = None
    ExecutionDate: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    DetailedStatus: StrictStr | None = None
    ExecutionSummary: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    OutputUrl: SSMInstanceAssociationOutputUrl | None = None
    AssociationName: StrictStr | None = None

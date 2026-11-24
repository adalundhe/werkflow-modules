from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerFlowDefinitionSummary(BaseModel):
    FlowDefinitionName: StrictStr | None = None
    FlowDefinitionArn: StrictStr | None = None
    FlowDefinitionStatus: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None

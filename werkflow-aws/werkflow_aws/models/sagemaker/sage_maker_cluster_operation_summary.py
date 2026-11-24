from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerClusterOperationSummary(BaseModel):
    OperationId: StrictStr | None = None
    ClusterArn: StrictStr | None = None
    Type: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None

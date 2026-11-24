from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class MSKClusterOperationV2Summary(BaseModel):
    ClusterArn: StrictStr | None = None
    ClusterType: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    OperationArn: StrictStr | None = None
    OperationState: StrictStr | None = None
    OperationType: StrictStr | None = None

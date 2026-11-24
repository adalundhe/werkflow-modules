from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerModelDashboardEndpoint(BaseModel):
    EndpointName: StrictStr | None = None
    EndpointArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    EndpointStatus: StrictStr | None = None

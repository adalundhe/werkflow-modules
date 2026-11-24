from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerEndpointConfigSummary(BaseModel):
    EndpointConfigName: StrictStr | None = None
    EndpointConfigArn: StrictStr | None = None
    CreationTime: datetime.datetime | None = None

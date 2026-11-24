from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_endpoint_status import SageMakerEndpointStatus


class SageMakerEndpointSummary(BaseModel):
    EndpointName: StrictStr | None = None
    EndpointArn: StrictStr | None = None
    CreationTime: datetime.datetime | None = None
    LastModifiedTime: datetime.datetime | None = None
    EndpointStatus: SageMakerEndpointStatus | None = None

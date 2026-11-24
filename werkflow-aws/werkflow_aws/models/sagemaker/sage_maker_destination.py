from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDestination(BaseModel):
    ResourceArn: StrictStr | None = None
    RoutingStatus: StrictStr | None = None

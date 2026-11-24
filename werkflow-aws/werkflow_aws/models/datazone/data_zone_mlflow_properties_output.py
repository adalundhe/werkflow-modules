from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneMlflowPropertiesOutput(BaseModel):
    trackingServerArn: StrictStr | None = None

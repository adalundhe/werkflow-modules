from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneMlflowPropertiesInput(BaseModel):
    trackingServerArn: StrictStr | None = None

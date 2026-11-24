from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneMlflowPropertiesPatch(BaseModel):
    trackingServerArn: StrictStr | None = None

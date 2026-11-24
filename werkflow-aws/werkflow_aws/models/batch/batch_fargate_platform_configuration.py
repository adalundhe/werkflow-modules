from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchFargatePlatformConfiguration(BaseModel):
    platformVersion: StrictStr | None = None

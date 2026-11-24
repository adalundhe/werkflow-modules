from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SageMakerInfraCheckConfig(BaseModel):
    EnableInfraCheck: StrictBool | None = None

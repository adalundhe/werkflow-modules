from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_retention_policy import SageMakerRetentionPolicy


class SageMakerDeleteDomainRequest(BaseModel):
    DomainId: StrictStr
    RetentionPolicy: SageMakerRetentionPolicy | None = None

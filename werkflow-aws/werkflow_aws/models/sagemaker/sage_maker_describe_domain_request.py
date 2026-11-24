from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeDomainRequest(BaseModel):
    DomainId: StrictStr

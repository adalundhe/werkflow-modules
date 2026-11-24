from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteSpaceRequest(BaseModel):
    DomainId: StrictStr
    SpaceName: StrictStr

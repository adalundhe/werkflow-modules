from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeSpaceRequest(BaseModel):
    DomainId: StrictStr
    SpaceName: StrictStr

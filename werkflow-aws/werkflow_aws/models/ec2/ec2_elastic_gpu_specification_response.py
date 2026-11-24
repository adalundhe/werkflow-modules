from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ElasticGpuSpecificationResponse(BaseModel):
    Type: StrictStr | None = None

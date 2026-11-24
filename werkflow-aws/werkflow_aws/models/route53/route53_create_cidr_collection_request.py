from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53CreateCidrCollectionRequest(BaseModel):
    Name: StrictStr
    CallerReference: StrictStr

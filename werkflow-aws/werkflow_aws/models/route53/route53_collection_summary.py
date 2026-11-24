from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class Route53CollectionSummary(BaseModel):
    Arn: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Version: StrictInt | None = None

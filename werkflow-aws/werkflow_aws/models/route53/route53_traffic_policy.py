from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class Route53TrafficPolicy(BaseModel):
    Id: StrictStr | None = None
    Version: StrictInt | None = None
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Document: StrictStr | None = None
    Comment: StrictStr | None = None

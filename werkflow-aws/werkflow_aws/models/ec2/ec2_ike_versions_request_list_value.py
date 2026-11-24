from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2IKEVersionsRequestListValue(BaseModel):
    Value: StrictStr | None = None

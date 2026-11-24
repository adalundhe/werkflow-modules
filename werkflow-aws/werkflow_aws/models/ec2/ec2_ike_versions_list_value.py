from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2IKEVersionsListValue(BaseModel):
    Value: StrictStr | None = None

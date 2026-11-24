from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2OperatorRequest(BaseModel):
    Principal: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAIAgent(BaseModel):
    Arn: StrictStr | None = None
    Type: StrictStr | None = None

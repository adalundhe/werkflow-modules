from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESSnsDestination(BaseModel):
    TopicArn: StrictStr | None = None

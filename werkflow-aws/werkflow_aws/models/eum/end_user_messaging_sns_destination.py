from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingSnsDestination(BaseModel):
    TopicArn: StrictStr | None = None

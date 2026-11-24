from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESTopic(BaseModel):
    TopicName: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Description: StrictStr | None = None
    DefaultSubscriptionStatus: StrictStr | None = None

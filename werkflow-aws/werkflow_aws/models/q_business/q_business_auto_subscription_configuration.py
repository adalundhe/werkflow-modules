from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessAutoSubscriptionConfiguration(BaseModel):
    autoSubscribe: StrictStr | None = None
    defaultSubscriptionType: StrictStr | None = None

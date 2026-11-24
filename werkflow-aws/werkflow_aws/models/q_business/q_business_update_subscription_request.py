from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QBusinessUpdateSubscriptionRequest(BaseModel):
    applicationId: StrictStr
    subscriptionId: StrictStr
    type: Literal['Q_LITE', 'Q_BUSINESS']

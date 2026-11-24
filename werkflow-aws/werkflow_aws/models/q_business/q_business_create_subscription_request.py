from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .q_business_subscription_principal import QBusinessSubscriptionPrincipal


class QBusinessCreateSubscriptionRequest(BaseModel):
    applicationId: StrictStr
    principal: QBusinessSubscriptionPrincipal
    type: Literal['Q_LITE', 'Q_BUSINESS']
    clientToken: StrictStr | None = None

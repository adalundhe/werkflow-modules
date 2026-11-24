from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_subscription_details import QBusinessSubscriptionDetails
from .q_business_subscription_principal import QBusinessSubscriptionPrincipal


class QBusinessSubscription(BaseModel):
    subscriptionId: StrictStr | None = None
    subscriptionArn: StrictStr | None = None
    principal: QBusinessSubscriptionPrincipal | None = None
    currentSubscription: QBusinessSubscriptionDetails | None = None
    nextSubscription: QBusinessSubscriptionDetails | None = None

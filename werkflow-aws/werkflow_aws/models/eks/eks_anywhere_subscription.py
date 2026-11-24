from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .eks_license import EKSLicense
from .eks_anywhere_subscription_term import EksAnywhereSubscriptionTerm


class EksAnywhereSubscription(BaseModel):
    id: StrictStr | None = None
    arn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    effectiveDate: datetime.datetime | StrictStr | None = None
    expirationDate: datetime.datetime | StrictStr | None = None
    licenseQuantity: StrictInt | None = None
    licenseType: StrictStr | None = None
    term: EksAnywhereSubscriptionTerm | None = None
    status: StrictStr | None = None
    autoRenew: StrictBool | None = None
    licenseArns: list[StrictStr] | None = None
    licenses: list[EKSLicense] | None = None
    tags: dict[StrictStr, StrictStr] | None = None

from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AppStreamAdminAppLicenseUsageRecord(BaseModel):
    UserArn: StrictStr | None = None
    BillingPeriod: StrictStr | None = None
    OwnerAWSAccountId: StrictStr | None = None
    SubscriptionFirstUsedDate: datetime.datetime | StrictStr | None = None
    SubscriptionLastUsedDate: datetime.datetime | StrictStr | None = None
    LicenseType: StrictStr | None = None
    UserId: StrictStr | None = None

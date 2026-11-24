from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_registered_customer_managed_key import QuickSightRegisteredCustomerManagedKey


class QuickSightUpdateKeyRegistrationRequest(BaseModel):
    AwsAccountId: StrictStr
    KeyRegistration: list[QuickSightRegisteredCustomerManagedKey]

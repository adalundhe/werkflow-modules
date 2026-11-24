from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_q_data_key import QuickSightQDataKey
from .quick_sight_registered_customer_managed_key import QuickSightRegisteredCustomerManagedKey


class QuickSightDescribeKeyRegistrationResponse(BaseModel):
    AwsAccountId: StrictStr | None = None
    KeyRegistration: list[QuickSightRegisteredCustomerManagedKey] | None = None
    QDataKey: QuickSightQDataKey | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None

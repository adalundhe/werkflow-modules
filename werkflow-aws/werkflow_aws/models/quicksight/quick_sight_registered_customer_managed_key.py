from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class QuickSightRegisteredCustomerManagedKey(BaseModel):
    KeyArn: StrictStr | None = None
    DefaultKey: StrictBool | None = None

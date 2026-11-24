from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightUpdateResourcePermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    RoleType: Literal['QUICKSIGHT_MANAGED', 'CUSTOMER_MANAGED']
    CustomerManagedRoleArn: StrictStr

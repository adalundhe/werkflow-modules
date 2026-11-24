from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CreateNetworkInterfacePermissionRequest(BaseModel):
    NetworkInterfaceId: StrictStr
    Permission: Literal['INSTANCE-ATTACH', 'EIP-ASSOCIATE']
    AwsAccountId: StrictStr | None = None
    AwsService: StrictStr | None = None
    DryRun: StrictBool | None = None

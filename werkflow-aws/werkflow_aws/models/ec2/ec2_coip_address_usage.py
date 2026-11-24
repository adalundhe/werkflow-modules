from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CoipAddressUsage(BaseModel):
    AllocationId: StrictStr | None = None
    AwsAccountId: StrictStr | None = None
    AwsService: StrictStr | None = None
    CoIp: StrictStr | None = None

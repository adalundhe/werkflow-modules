from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2DescribeIdentityIdFormatRequest(BaseModel):
    PrincipalArn: StrictStr
    Resource: StrictStr | None = None

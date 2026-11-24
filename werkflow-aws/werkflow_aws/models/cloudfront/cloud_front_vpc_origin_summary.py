from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudFrontVpcOriginSummary(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    Arn: StrictStr | None = None
    AccountId: StrictStr | None = None
    OriginEndpointArn: StrictStr | None = None
    IpAddressType: StrictStr | None = None

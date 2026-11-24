from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_ipam_config import CloudFrontIpamConfig


class CloudFrontAnycastIpListSummary(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    Arn: StrictStr | None = None
    IpCount: StrictInt | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    IpAddressType: StrictStr | None = None
    ETag: StrictStr | None = None
    IpamConfig: CloudFrontIpamConfig | None = None

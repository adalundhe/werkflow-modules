from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_front_key_group_config import CloudFrontKeyGroupConfig


class CloudFrontKeyGroup(BaseModel):
    Id: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    KeyGroupConfig: CloudFrontKeyGroupConfig | None = None

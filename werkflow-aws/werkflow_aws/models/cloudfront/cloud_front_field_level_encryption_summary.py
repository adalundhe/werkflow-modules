from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_front_content_type_profile_config import CloudFrontContentTypeProfileConfig
from .cloud_front_query_arg_profile_config import CloudFrontQueryArgProfileConfig


class CloudFrontFieldLevelEncryptionSummary(BaseModel):
    Id: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    Comment: StrictStr | None = None
    QueryArgProfileConfig: CloudFrontQueryArgProfileConfig | None = None
    ContentTypeProfileConfig: CloudFrontContentTypeProfileConfig | None = None

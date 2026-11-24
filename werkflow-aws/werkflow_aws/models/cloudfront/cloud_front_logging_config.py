from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFrontLoggingConfig(BaseModel):
    Enabled: StrictBool | None = None
    IncludeCookies: StrictBool | None = None
    Bucket: StrictStr | None = None
    Prefix: StrictStr | None = None

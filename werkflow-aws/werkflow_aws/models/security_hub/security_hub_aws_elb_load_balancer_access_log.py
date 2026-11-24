from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SecurityHubAwsElbLoadBalancerAccessLog(BaseModel):
    EmitInterval: StrictInt | None = None
    Enabled: StrictBool | None = None
    S3BucketName: StrictStr | None = None
    S3BucketPrefix: StrictStr | None = None

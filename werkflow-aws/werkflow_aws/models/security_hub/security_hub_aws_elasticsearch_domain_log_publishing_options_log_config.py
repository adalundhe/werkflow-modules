from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsElasticsearchDomainLogPublishingOptionsLogConfig(BaseModel):
    CloudWatchLogsLogGroupArn: StrictStr | None = None
    Enabled: StrictBool | None = None

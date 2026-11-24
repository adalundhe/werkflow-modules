from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsAppSyncGraphQlApiLogConfigDetails(BaseModel):
    CloudWatchLogsRoleArn: StrictStr | None = None
    ExcludeVerboseContent: StrictBool | None = None
    FieldLogLevel: StrictStr | None = None

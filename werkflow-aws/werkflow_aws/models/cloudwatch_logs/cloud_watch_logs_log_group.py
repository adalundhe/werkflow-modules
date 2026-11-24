from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class CloudWatchLogsLogGroup(BaseModel):
    logGroupName: StrictStr | None = None
    creationTime: StrictInt | None = None
    retentionInDays: StrictInt | None = None
    metricFilterCount: StrictInt | None = None
    arn: StrictStr | None = None
    storedBytes: StrictInt | None = None
    kmsKeyId: StrictStr | None = None
    dataProtectionStatus: StrictStr | None = None
    inheritedProperties: list[StrictStr] | None = None
    logGroupClass: StrictStr | None = None
    logGroupArn: StrictStr | None = None
    deletionProtectionEnabled: StrictBool | None = None
    bearerTokenAuthenticationEnabled: StrictBool | None = None
    retentionPolicyName: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_lake_aws_identity import SecurityLakeAwsIdentity
from .security_lake_log_source_resource import SecurityLakeLogSourceResource


class SecurityLakeUpdateSubscriberRequest(BaseModel):
    subscriberId: StrictStr
    sources: list[SecurityLakeLogSourceResource] | None = None
    subscriberDescription: StrictStr | None = None
    subscriberIdentity: SecurityLakeAwsIdentity | None = None
    subscriberName: StrictStr | None = None

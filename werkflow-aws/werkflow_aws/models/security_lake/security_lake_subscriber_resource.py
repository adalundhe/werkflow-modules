from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .security_lake_aws_identity import SecurityLakeAwsIdentity
from .security_lake_log_source_resource import SecurityLakeLogSourceResource


class SecurityLakeSubscriberResource(BaseModel):
    accessTypes: list[StrictStr] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    resourceShareArn: StrictStr | None = None
    resourceShareName: StrictStr | None = None
    roleArn: StrictStr | None = None
    s3BucketArn: StrictStr | None = None
    sources: list[SecurityLakeLogSourceResource] | None = None
    subscriberArn: StrictStr | None = None
    subscriberDescription: StrictStr | None = None
    subscriberEndpoint: StrictStr | None = None
    subscriberId: StrictStr | None = None
    subscriberIdentity: SecurityLakeAwsIdentity | None = None
    subscriberName: StrictStr | None = None
    subscriberStatus: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None

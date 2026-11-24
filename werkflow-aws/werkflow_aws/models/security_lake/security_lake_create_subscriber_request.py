from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .security_lake_aws_identity import SecurityLakeAwsIdentity
from .security_lake_log_source_resource import SecurityLakeLogSourceResource
from .security_lake_tag import SecurityLakeTag


class SecurityLakeCreateSubscriberRequest(BaseModel):
    sources: list[SecurityLakeLogSourceResource]
    subscriberIdentity: SecurityLakeAwsIdentity
    subscriberName: StrictStr
    accessTypes: list[Literal['LAKEFORMATION', 'S3']] | None = None
    subscriberDescription: StrictStr | None = None
    tags: list[SecurityLakeTag] | None = None

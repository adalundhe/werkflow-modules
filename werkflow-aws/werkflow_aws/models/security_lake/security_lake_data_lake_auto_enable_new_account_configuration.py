from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_lake_aws_log_source_resource import SecurityLakeAwsLogSourceResource


class SecurityLakeDataLakeAutoEnableNewAccountConfiguration(BaseModel):
    region: StrictStr | None = None
    sources: list[SecurityLakeAwsLogSourceResource] | None = None

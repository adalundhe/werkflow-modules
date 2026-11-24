from __future__ import annotations
from pydantic import BaseModel
from .security_lake_aws_log_source_resource import SecurityLakeAwsLogSourceResource
from .security_lake_custom_log_source_resource import SecurityLakeCustomLogSourceResource


class SecurityLakeLogSourceResource(BaseModel):
    awsLogSource: SecurityLakeAwsLogSourceResource | None = None
    customLogSource: SecurityLakeCustomLogSourceResource | None = None

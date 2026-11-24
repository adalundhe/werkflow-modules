from __future__ import annotations
from pydantic import BaseModel
from .security_lake_aws_log_source_configuration import SecurityLakeAwsLogSourceConfiguration


class SecurityLakeDeleteAwsLogSourceRequest(BaseModel):
    sources: list[SecurityLakeAwsLogSourceConfiguration]

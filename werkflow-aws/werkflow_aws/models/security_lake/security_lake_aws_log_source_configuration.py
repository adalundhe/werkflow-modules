from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SecurityLakeAwsLogSourceConfiguration(BaseModel):
    regions: list[StrictStr]
    sourceName: Literal['ROUTE53', 'VPC_FLOW', 'SH_FINDINGS', 'CLOUD_TRAIL_MGMT', 'LAMBDA_EXECUTION', 'S3_DATA', 'EKS_AUDIT', 'WAF']
    accounts: list[StrictStr] | None = None
    sourceVersion: StrictStr | None = None

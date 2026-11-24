from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsRedshiftClusterElasticIpStatus(BaseModel):
    ElasticIp: StrictStr | None = None
    Status: StrictStr | None = None

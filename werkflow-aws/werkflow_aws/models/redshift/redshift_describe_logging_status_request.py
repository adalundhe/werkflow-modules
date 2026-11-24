from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDescribeLoggingStatusRequest(BaseModel):
    ClusterIdentifier: StrictStr

from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class RedshiftDisableLoggingRequest(BaseModel):
    ClusterIdentifier: StrictStr
    LogDestinationType: Literal['s3', 'cloudwatch', 's3table'] | None = None
    LogExports: list[StrictStr] | None = None

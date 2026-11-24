from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class MacieSearchResourcesSimpleCriterion(BaseModel):
    comparator: Literal['EQ', 'NE'] | None = None
    key: Literal['ACCOUNT_ID', 'S3_BUCKET_NAME', 'S3_BUCKET_EFFECTIVE_PERMISSION', 'S3_BUCKET_SHARED_ACCESS', 'AUTOMATED_DISCOVERY_MONITORING_STATUS'] | None = None
    values: list[StrictStr] | None = None

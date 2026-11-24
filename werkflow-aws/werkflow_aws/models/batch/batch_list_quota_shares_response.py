from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .batch_quota_share_detail import BatchQuotaShareDetail


class BatchListQuotaSharesResponse(BaseModel):
    quotaShares: list[BatchQuotaShareDetail] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

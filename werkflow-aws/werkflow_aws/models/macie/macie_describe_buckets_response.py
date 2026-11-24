from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_bucket_metadata import MacieBucketMetadata


class MacieDescribeBucketsResponse(BaseModel):
    buckets: list[MacieBucketMetadata] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

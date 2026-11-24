from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_invalidation_batch import CloudFrontInvalidationBatch


class CloudFrontCreateInvalidationRequest(BaseModel):
    DistributionId: StrictStr
    InvalidationBatch: CloudFrontInvalidationBatch

from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_front_invalidation_batch import CloudFrontInvalidationBatch


class CloudFrontInvalidation(BaseModel):
    Id: StrictStr | None = None
    Status: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    InvalidationBatch: CloudFrontInvalidationBatch | None = None

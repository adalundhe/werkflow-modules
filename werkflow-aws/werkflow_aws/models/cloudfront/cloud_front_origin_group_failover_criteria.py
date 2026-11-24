from __future__ import annotations
from pydantic import BaseModel
from .cloud_front_status_codes import CloudFrontStatusCodes


class CloudFrontOriginGroupFailoverCriteria(BaseModel):
    StatusCodes: CloudFrontStatusCodes | None = None

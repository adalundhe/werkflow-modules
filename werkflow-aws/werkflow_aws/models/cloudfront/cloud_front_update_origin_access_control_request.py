from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_origin_access_control_config import CloudFrontOriginAccessControlConfig


class CloudFrontUpdateOriginAccessControlRequest(BaseModel):
    OriginAccessControlConfig: CloudFrontOriginAccessControlConfig
    Id: StrictStr
    IfMatch: StrictStr | None = None

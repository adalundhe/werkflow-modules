from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_origin_access_control_config import CloudFrontOriginAccessControlConfig


class CloudFrontOriginAccessControl(BaseModel):
    Id: StrictStr | None = None
    OriginAccessControlConfig: CloudFrontOriginAccessControlConfig | None = None

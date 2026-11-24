from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_front_public_key_config import CloudFrontPublicKeyConfig


class CloudFrontPublicKey(BaseModel):
    Id: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    PublicKeyConfig: CloudFrontPublicKeyConfig | None = None

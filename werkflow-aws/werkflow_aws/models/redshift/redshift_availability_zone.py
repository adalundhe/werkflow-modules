from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_supported_platform import RedshiftSupportedPlatform


class RedshiftAvailabilityZone(BaseModel):
    Name: StrictStr | None = None
    SupportedPlatforms: list[RedshiftSupportedPlatform] | None = None

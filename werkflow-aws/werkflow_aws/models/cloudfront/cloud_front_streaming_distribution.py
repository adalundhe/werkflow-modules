from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_front_active_trusted_signers import CloudFrontActiveTrustedSigners
from .cloud_front_streaming_distribution_config import CloudFrontStreamingDistributionConfig


class CloudFrontStreamingDistribution(BaseModel):
    Id: StrictStr | None = None
    ARN: StrictStr | None = None
    Status: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    DomainName: StrictStr | None = None
    ActiveTrustedSigners: CloudFrontActiveTrustedSigners | None = None
    StreamingDistributionConfig: CloudFrontStreamingDistributionConfig | None = None

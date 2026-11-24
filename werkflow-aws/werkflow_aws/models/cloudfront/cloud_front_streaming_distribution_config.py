from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_front_aliases import CloudFrontAliases
from .cloud_front_s3_origin import CloudFrontS3Origin
from .cloud_front_streaming_logging_config import CloudFrontStreamingLoggingConfig
from .cloud_front_trusted_signers import CloudFrontTrustedSigners


class CloudFrontStreamingDistributionConfig(BaseModel):
    CallerReference: StrictStr | None = None
    S3Origin: CloudFrontS3Origin | None = None
    Aliases: CloudFrontAliases | None = None
    Comment: StrictStr | None = None
    Logging: CloudFrontStreamingLoggingConfig | None = None
    TrustedSigners: CloudFrontTrustedSigners | None = None
    PriceClass: StrictStr | None = None
    Enabled: StrictBool | None = None

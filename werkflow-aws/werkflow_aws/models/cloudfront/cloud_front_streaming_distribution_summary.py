from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_front_aliases import CloudFrontAliases
from .cloud_front_s3_origin import CloudFrontS3Origin
from .cloud_front_trusted_signers import CloudFrontTrustedSigners


class CloudFrontStreamingDistributionSummary(BaseModel):
    Id: StrictStr | None = None
    ARN: StrictStr | None = None
    Status: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    DomainName: StrictStr | None = None
    S3Origin: CloudFrontS3Origin | None = None
    Aliases: CloudFrontAliases | None = None
    TrustedSigners: CloudFrontTrustedSigners | None = None
    Comment: StrictStr | None = None
    PriceClass: StrictStr | None = None
    Enabled: StrictBool | None = None

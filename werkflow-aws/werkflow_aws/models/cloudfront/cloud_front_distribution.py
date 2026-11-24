from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_active_trusted_key_groups import CloudFrontActiveTrustedKeyGroups
from .cloud_front_active_trusted_signers import CloudFrontActiveTrustedSigners
from .cloud_front_alias_icp_recordal import CloudFrontAliasICPRecordal
from .cloud_front_distribution_config import CloudFrontDistributionConfig


class CloudFrontDistribution(BaseModel):
    Id: StrictStr | None = None
    ARN: StrictStr | None = None
    Status: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    InProgressInvalidationBatches: StrictInt | None = None
    DomainName: StrictStr | None = None
    ActiveTrustedSigners: CloudFrontActiveTrustedSigners | None = None
    ActiveTrustedKeyGroups: CloudFrontActiveTrustedKeyGroups | None = None
    DistributionConfig: CloudFrontDistributionConfig | None = None
    AliasICPRecordals: list[CloudFrontAliasICPRecordal] | None = None

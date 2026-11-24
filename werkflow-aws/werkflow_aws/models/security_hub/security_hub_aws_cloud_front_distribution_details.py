from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_cloud_front_distribution_cache_behaviors import SecurityHubAwsCloudFrontDistributionCacheBehaviors
from .security_hub_aws_cloud_front_distribution_default_cache_behavior import SecurityHubAwsCloudFrontDistributionDefaultCacheBehavior
from .security_hub_aws_cloud_front_distribution_logging import SecurityHubAwsCloudFrontDistributionLogging
from .security_hub_aws_cloud_front_distribution_origin_groups import SecurityHubAwsCloudFrontDistributionOriginGroups
from .security_hub_aws_cloud_front_distribution_origins import SecurityHubAwsCloudFrontDistributionOrigins
from .security_hub_aws_cloud_front_distribution_viewer_certificate import SecurityHubAwsCloudFrontDistributionViewerCertificate


class SecurityHubAwsCloudFrontDistributionDetails(BaseModel):
    CacheBehaviors: SecurityHubAwsCloudFrontDistributionCacheBehaviors | None = None
    DefaultCacheBehavior: SecurityHubAwsCloudFrontDistributionDefaultCacheBehavior | None = None
    DefaultRootObject: StrictStr | None = None
    DomainName: StrictStr | None = None
    ETag: StrictStr | None = None
    LastModifiedTime: StrictStr | None = None
    Logging: SecurityHubAwsCloudFrontDistributionLogging | None = None
    Origins: SecurityHubAwsCloudFrontDistributionOrigins | None = None
    OriginGroups: SecurityHubAwsCloudFrontDistributionOriginGroups | None = None
    ViewerCertificate: SecurityHubAwsCloudFrontDistributionViewerCertificate | None = None
    Status: StrictStr | None = None
    WebAclId: StrictStr | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_front_aliases import CloudFrontAliases
from .cloud_front_cache_behaviors import CloudFrontCacheBehaviors
from .cloud_front_cache_tag_config import CloudFrontCacheTagConfig
from .cloud_front_connection_function_association import CloudFrontConnectionFunctionAssociation
from .cloud_front_custom_error_responses import CloudFrontCustomErrorResponses
from .cloud_front_default_cache_behavior import CloudFrontDefaultCacheBehavior
from .cloud_front_logging_config import CloudFrontLoggingConfig
from .cloud_front_origin_groups import CloudFrontOriginGroups
from .cloud_front_origins import CloudFrontOrigins
from .cloud_front_restrictions import CloudFrontRestrictions
from .cloud_front_tenant_config import CloudFrontTenantConfig
from .cloud_front_viewer_certificate import CloudFrontViewerCertificate
from .cloud_front_viewer_mtls_config import CloudFrontViewerMtlsConfig


class CloudFrontDistributionConfig(BaseModel):
    CallerReference: StrictStr | None = None
    Aliases: CloudFrontAliases | None = None
    DefaultRootObject: StrictStr | None = None
    Origins: CloudFrontOrigins | None = None
    OriginGroups: CloudFrontOriginGroups | None = None
    DefaultCacheBehavior: CloudFrontDefaultCacheBehavior | None = None
    CacheBehaviors: CloudFrontCacheBehaviors | None = None
    CustomErrorResponses: CloudFrontCustomErrorResponses | None = None
    Comment: StrictStr | None = None
    Logging: CloudFrontLoggingConfig | None = None
    PriceClass: StrictStr | None = None
    Enabled: StrictBool | None = None
    ViewerCertificate: CloudFrontViewerCertificate | None = None
    Restrictions: CloudFrontRestrictions | None = None
    WebACLId: StrictStr | None = None
    HttpVersion: StrictStr | None = None
    IsIPV6Enabled: StrictBool | None = None
    ContinuousDeploymentPolicyId: StrictStr | None = None
    Staging: StrictBool | None = None
    AnycastIpListId: StrictStr | None = None
    TenantConfig: CloudFrontTenantConfig | None = None
    ConnectionMode: StrictStr | None = None
    ViewerMtlsConfig: CloudFrontViewerMtlsConfig | None = None
    ConnectionFunctionAssociation: CloudFrontConnectionFunctionAssociation | None = None
    CacheTagConfig: CloudFrontCacheTagConfig | None = None

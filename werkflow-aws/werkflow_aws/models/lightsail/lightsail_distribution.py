from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .lightsail_cache_behavior import LightsailCacheBehavior
from .lightsail_cache_behavior_per_path import LightsailCacheBehaviorPerPath
from .lightsail_cache_settings import LightsailCacheSettings
from .lightsail_distribution_custom_error_response import LightsailDistributionCustomErrorResponse
from .lightsail_distribution_subdomain import LightsailDistributionSubdomain
from .lightsail_origin import LightsailOrigin
from .lightsail_resource_location import LightsailResourceLocation
from .lightsail_tag import LightsailTag
from .lightsail_waf_config import LightsailWafConfig


class LightsailDistribution(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    supportCode: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    location: LightsailResourceLocation | None = None
    resourceType: StrictStr | None = None
    alternativeDomainNames: list[StrictStr] | None = None
    status: StrictStr | None = None
    isEnabled: StrictBool | None = None
    domainName: StrictStr | None = None
    bundleId: StrictStr | None = None
    certificateName: StrictStr | None = None
    origin: LightsailOrigin | None = None
    originPublicDNS: StrictStr | None = None
    defaultCacheBehavior: LightsailCacheBehavior | None = None
    cacheBehaviorSettings: LightsailCacheSettings | None = None
    cacheBehaviors: list[LightsailCacheBehaviorPerPath] | None = None
    ableToUpdateBundle: StrictBool | None = None
    ipAddressType: StrictStr | None = None
    tags: list[LightsailTag] | None = None
    viewerMinimumTlsProtocolVersion: StrictStr | None = None
    defaultRootObject: StrictStr | None = None
    customErrorResponses: list[LightsailDistributionCustomErrorResponse] | None = None
    waf: LightsailWafConfig | None = None
    subdomain: LightsailDistributionSubdomain | None = None

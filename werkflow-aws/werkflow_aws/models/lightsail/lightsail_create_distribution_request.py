from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .lightsail_cache_behavior import LightsailCacheBehavior
from .lightsail_cache_behavior_per_path import LightsailCacheBehaviorPerPath
from .lightsail_cache_settings import LightsailCacheSettings
from .lightsail_distribution_custom_error_response import LightsailDistributionCustomErrorResponse
from .lightsail_input_origin import LightsailInputOrigin
from .lightsail_tag import LightsailTag
from .lightsail_waf_rule import LightsailWafRule


class LightsailCreateDistributionRequest(BaseModel):
    distributionName: StrictStr
    origin: LightsailInputOrigin
    defaultCacheBehavior: LightsailCacheBehavior
    bundleId: StrictStr
    cacheBehaviorSettings: LightsailCacheSettings | None = None
    cacheBehaviors: list[LightsailCacheBehaviorPerPath] | None = None
    ipAddressType: Literal['dualstack', 'ipv4', 'ipv6'] | None = None
    tags: list[LightsailTag] | None = None
    certificateName: StrictStr | None = None
    viewerMinimumTlsProtocolVersion: Literal['TLSv1.1_2016', 'TLSv1.2_2018', 'TLSv1.2_2019', 'TLSv1.2_2021'] | None = None
    enablePrivateOriginAccess: StrictBool | None = None
    defaultRootObject: StrictStr | None = None
    customErrorResponses: list[LightsailDistributionCustomErrorResponse] | None = None
    enableWaf: StrictBool | None = None
    wafRules: list[LightsailWafRule] | None = None
    subdomainName: StrictStr | None = None

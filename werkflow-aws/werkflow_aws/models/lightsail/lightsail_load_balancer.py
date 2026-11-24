from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .lightsail_instance_health_summary import LightsailInstanceHealthSummary
from .lightsail_load_balancer_tls_certificate_summary import LightsailLoadBalancerTlsCertificateSummary
from .lightsail_resource_location import LightsailResourceLocation
from .lightsail_tag import LightsailTag


class LightsailLoadBalancer(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    supportCode: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    location: LightsailResourceLocation | None = None
    resourceType: StrictStr | None = None
    tags: list[LightsailTag] | None = None
    dnsName: StrictStr | None = None
    state: StrictStr | None = None
    protocol: StrictStr | None = None
    publicPorts: list[StrictInt] | None = None
    healthCheckPath: StrictStr | None = None
    instancePort: StrictInt | None = None
    instanceHealthSummary: list[LightsailInstanceHealthSummary] | None = None
    tlsCertificateSummaries: list[LightsailLoadBalancerTlsCertificateSummary] | None = None
    configurationOptions: dict[StrictStr, StrictStr] | None = None
    ipAddressType: StrictStr | None = None
    httpsRedirectionEnabled: StrictBool | None = None
    tlsPolicyName: StrictStr | None = None

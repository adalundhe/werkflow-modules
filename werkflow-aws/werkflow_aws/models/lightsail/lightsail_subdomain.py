from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .lightsail_resource_location import LightsailResourceLocation
from .lightsail_subdomain_attachable_resource import LightsailSubdomainAttachableResource
from .lightsail_tag import LightsailTag


class LightsailSubdomain(BaseModel):
    subdomainName: StrictStr | None = None
    arn: StrictStr | None = None
    fqdn: StrictStr | None = None
    depth: StrictInt | None = None
    state: StrictStr | None = None
    attachedResource: LightsailSubdomainAttachableResource | None = None
    attachingResource: LightsailSubdomainAttachableResource | None = None
    location: LightsailResourceLocation | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    parentFqdn: StrictStr | None = None
    children: list[LightsailSubdomain] | None = None
    tags: list[LightsailTag] | None = None

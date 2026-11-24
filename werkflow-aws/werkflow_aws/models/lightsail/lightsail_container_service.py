from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .lightsail_container_service_deployment import LightsailContainerServiceDeployment
from .lightsail_container_service_state_detail import LightsailContainerServiceStateDetail
from .lightsail_private_registry_access import LightsailPrivateRegistryAccess
from .lightsail_resource_location import LightsailResourceLocation
from .lightsail_tag import LightsailTag


class LightsailContainerService(BaseModel):
    containerServiceName: StrictStr | None = None
    arn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    location: LightsailResourceLocation | None = None
    resourceType: StrictStr | None = None
    tags: list[LightsailTag] | None = None
    power: StrictStr | None = None
    powerId: StrictStr | None = None
    state: StrictStr | None = None
    stateDetail: LightsailContainerServiceStateDetail | None = None
    scale: StrictInt | None = None
    currentDeployment: LightsailContainerServiceDeployment | None = None
    nextDeployment: LightsailContainerServiceDeployment | None = None
    isDisabled: StrictBool | None = None
    principalArn: StrictStr | None = None
    privateDomainName: StrictStr | None = None
    publicDomainNames: dict[StrictStr, list[StrictStr]] | None = None
    url: StrictStr | None = None
    privateRegistryAccess: LightsailPrivateRegistryAccess | None = None

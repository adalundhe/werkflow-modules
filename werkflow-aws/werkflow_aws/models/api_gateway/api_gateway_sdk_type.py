from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_sdk_configuration_property import APIGatewaySdkConfigurationProperty


class APIGatewaySdkType(BaseModel):
    id: StrictStr | None = None
    friendlyName: StrictStr | None = None
    description: StrictStr | None = None
    configurationProperties: list[APIGatewaySdkConfigurationProperty] | None = None

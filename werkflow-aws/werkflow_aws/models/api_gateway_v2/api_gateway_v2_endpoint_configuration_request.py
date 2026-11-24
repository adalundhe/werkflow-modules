from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
from .api_gateway_v2_acm_managed import APIGatewayV2ACMManaged
from .api_gateway_v2_none import APIGatewayV2None


class APIGatewayV2EndpointConfigurationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    AcmManaged: APIGatewayV2ACMManaged | None = None
    None_: APIGatewayV2None | None = Field(default=None, alias='None')

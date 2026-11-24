from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
from .api_gateway_v2_cognito_config import APIGatewayV2CognitoConfig
from .api_gateway_v2_none import APIGatewayV2None


class APIGatewayV2Authorization(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    CognitoConfig: APIGatewayV2CognitoConfig | None = None
    None_: APIGatewayV2None | None = Field(default=None, alias='None')

from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2DeleteCorsConfigurationRequest(BaseModel):
    ApiId: StrictStr

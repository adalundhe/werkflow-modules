from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .bedrock_endpoint_config import BedrockEndpointConfig


class BedrockMarketplaceModelEndpoint(BaseModel):
    endpointArn: StrictStr | None = None
    modelSourceIdentifier: StrictStr | None = None
    status: StrictStr | None = None
    statusMessage: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    endpointConfig: BedrockEndpointConfig | None = None
    endpointStatus: StrictStr | None = None
    endpointStatusMessage: StrictStr | None = None

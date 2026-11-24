from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_method_snapshot import APIGatewayMethodSnapshot


class APIGatewayGetDeploymentResponse(BaseModel):
    id: StrictStr | None = None
    description: StrictStr | None = None
    createdDate: datetime.datetime | StrictStr | None = None
    apiSummary: dict[StrictStr, dict[StrictStr, APIGatewayMethodSnapshot]] | None = None
    ResponseMetadata: dict[str, Any] | None = None

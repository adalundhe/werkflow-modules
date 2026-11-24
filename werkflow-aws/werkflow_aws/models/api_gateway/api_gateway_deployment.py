from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .api_gateway_method_snapshot import APIGatewayMethodSnapshot


class APIGatewayDeployment(BaseModel):
    id: StrictStr | None = None
    description: StrictStr | None = None
    createdDate: datetime.datetime | StrictStr | None = None
    apiSummary: dict[StrictStr, dict[StrictStr, APIGatewayMethodSnapshot]] | None = None

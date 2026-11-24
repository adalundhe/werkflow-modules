from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayV2Deployment(BaseModel):
    AutoDeployed: StrictBool | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    DeploymentId: StrictStr | None = None
    DeploymentStatus: StrictStr | None = None
    DeploymentStatusMessage: StrictStr | None = None
    Description: StrictStr | None = None

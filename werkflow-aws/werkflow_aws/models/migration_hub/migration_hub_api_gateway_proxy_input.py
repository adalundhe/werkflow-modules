from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubApiGatewayProxyInput(BaseModel):
    EndpointType: StrictStr | None = None
    StageName: StrictStr | None = None

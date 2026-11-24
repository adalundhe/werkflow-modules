from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubApiGatewayProxyConfig(BaseModel):
    ApiGatewayId: StrictStr | None = None
    EndpointType: StrictStr | None = None
    NlbArn: StrictStr | None = None
    NlbName: StrictStr | None = None
    ProxyUrl: StrictStr | None = None
    StageName: StrictStr | None = None
    VpcLinkId: StrictStr | None = None

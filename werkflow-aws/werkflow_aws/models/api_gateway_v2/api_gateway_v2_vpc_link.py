from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class APIGatewayV2VpcLink(BaseModel):
    CreatedDate: datetime.datetime | StrictStr | None = None
    Name: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    SubnetIds: list[StrictStr] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    VpcLinkId: StrictStr | None = None
    VpcLinkStatus: StrictStr | None = None
    VpcLinkStatusMessage: StrictStr | None = None
    VpcLinkVersion: StrictStr | None = None

from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class APIGatewayV2UpdateVpcLinkResponse(BaseModel):
    CreatedDate: datetime.datetime | StrictStr | None = None
    Name: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    SubnetIds: list[StrictStr] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    VpcLinkId: StrictStr | None = None
    VpcLinkStatus: StrictStr | None = None
    VpcLinkStatusMessage: StrictStr | None = None
    VpcLinkVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

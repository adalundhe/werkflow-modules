from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectDescribeRouterConfigurationRequest(BaseModel):
    virtualInterfaceId: StrictStr
    routerTypeIdentifier: StrictStr | None = None

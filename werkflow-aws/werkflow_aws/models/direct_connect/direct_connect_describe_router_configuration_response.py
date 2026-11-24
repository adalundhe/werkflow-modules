from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .direct_connect_router_type import DirectConnectRouterType


class DirectConnectDescribeRouterConfigurationResponse(BaseModel):
    customerRouterConfig: StrictStr | None = None
    router: DirectConnectRouterType | None = None
    virtualInterfaceId: StrictStr | None = None
    virtualInterfaceName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

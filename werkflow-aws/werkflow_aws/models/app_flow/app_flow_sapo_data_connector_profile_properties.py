from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .app_flow_o_auth_properties import AppFlowOAuthProperties


class AppFlowSAPODataConnectorProfileProperties(BaseModel):
    applicationHostUrl: StrictStr | None = None
    applicationServicePath: StrictStr | None = None
    portNumber: StrictInt | None = None
    clientNumber: StrictStr | None = None
    logonLanguage: StrictStr | None = None
    privateLinkServiceName: StrictStr | None = None
    oAuthProperties: AppFlowOAuthProperties | None = None
    disableSSO: StrictBool | None = None

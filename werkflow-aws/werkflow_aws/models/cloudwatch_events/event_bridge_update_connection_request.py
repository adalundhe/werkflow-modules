from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .event_bridge_connectivity_resource_parameters import EventBridgeConnectivityResourceParameters
from .event_bridge_update_connection_auth_request_parameters import EventBridgeUpdateConnectionAuthRequestParameters


class EventBridgeUpdateConnectionRequest(BaseModel):
    Name: StrictStr
    Description: StrictStr | None = None
    AuthorizationType: Literal['BASIC', 'OAUTH_CLIENT_CREDENTIALS', 'API_KEY'] | None = None
    AuthParameters: EventBridgeUpdateConnectionAuthRequestParameters | None = None
    InvocationConnectivityParameters: EventBridgeConnectivityResourceParameters | None = None
    KmsKeyIdentifier: StrictStr | None = None

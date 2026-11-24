from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .event_bridge_connectivity_resource_parameters import EventBridgeConnectivityResourceParameters
from .event_bridge_create_connection_auth_request_parameters import EventBridgeCreateConnectionAuthRequestParameters


class EventBridgeCreateConnectionRequest(BaseModel):
    Name: StrictStr
    AuthorizationType: Literal['BASIC', 'OAUTH_CLIENT_CREDENTIALS', 'API_KEY']
    AuthParameters: EventBridgeCreateConnectionAuthRequestParameters
    Description: StrictStr | None = None
    InvocationConnectivityParameters: EventBridgeConnectivityResourceParameters | None = None
    KmsKeyIdentifier: StrictStr | None = None

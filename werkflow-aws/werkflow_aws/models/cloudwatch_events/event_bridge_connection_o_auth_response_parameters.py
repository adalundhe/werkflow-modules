from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .event_bridge_connection_http_parameters import EventBridgeConnectionHttpParameters
from .event_bridge_connection_o_auth_client_response_parameters import EventBridgeConnectionOAuthClientResponseParameters


class EventBridgeConnectionOAuthResponseParameters(BaseModel):
    ClientParameters: EventBridgeConnectionOAuthClientResponseParameters | None = None
    AuthorizationEndpoint: StrictStr | None = None
    HttpMethod: StrictStr | None = None
    OAuthHttpParameters: EventBridgeConnectionHttpParameters | None = None

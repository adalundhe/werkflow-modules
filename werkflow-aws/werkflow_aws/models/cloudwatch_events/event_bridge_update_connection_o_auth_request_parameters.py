from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .event_bridge_connection_http_parameters import EventBridgeConnectionHttpParameters
from .event_bridge_update_connection_o_auth_client_request_parameters import EventBridgeUpdateConnectionOAuthClientRequestParameters


class EventBridgeUpdateConnectionOAuthRequestParameters(BaseModel):
    ClientParameters: EventBridgeUpdateConnectionOAuthClientRequestParameters | None = None
    AuthorizationEndpoint: StrictStr | None = None
    HttpMethod: Literal['GET', 'POST', 'PUT'] | None = None
    OAuthHttpParameters: EventBridgeConnectionHttpParameters | None = None

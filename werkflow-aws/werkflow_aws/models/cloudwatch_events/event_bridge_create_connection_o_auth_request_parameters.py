from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .event_bridge_connection_http_parameters import EventBridgeConnectionHttpParameters
from .event_bridge_create_connection_o_auth_client_request_parameters import EventBridgeCreateConnectionOAuthClientRequestParameters


class EventBridgeCreateConnectionOAuthRequestParameters(BaseModel):
    ClientParameters: EventBridgeCreateConnectionOAuthClientRequestParameters
    AuthorizationEndpoint: StrictStr
    HttpMethod: Literal['GET', 'POST', 'PUT']
    OAuthHttpParameters: EventBridgeConnectionHttpParameters | None = None

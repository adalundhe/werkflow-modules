from __future__ import annotations
from pydantic import BaseModel
from .event_bridge_connection_body_parameter import EventBridgeConnectionBodyParameter
from .event_bridge_connection_header_parameter import EventBridgeConnectionHeaderParameter
from .event_bridge_connection_query_string_parameter import EventBridgeConnectionQueryStringParameter


class EventBridgeConnectionHttpParameters(BaseModel):
    HeaderParameters: list[EventBridgeConnectionHeaderParameter] | None = None
    QueryStringParameters: list[EventBridgeConnectionQueryStringParameter] | None = None
    BodyParameters: list[EventBridgeConnectionBodyParameter] | None = None

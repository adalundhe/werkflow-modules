from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .event_bridge_connection_auth_response_parameters import EventBridgeConnectionAuthResponseParameters
from .event_bridge_describe_connection_connectivity_parameters import EventBridgeDescribeConnectionConnectivityParameters


class EventBridgeDescribeConnectionResponse(BaseModel):
    ConnectionArn: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    InvocationConnectivityParameters: EventBridgeDescribeConnectionConnectivityParameters | None = None
    ConnectionState: StrictStr | None = None
    StateReason: StrictStr | None = None
    AuthorizationType: StrictStr | None = None
    SecretArn: StrictStr | None = None
    KmsKeyIdentifier: StrictStr | None = None
    AuthParameters: EventBridgeConnectionAuthResponseParameters | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastAuthorizedTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

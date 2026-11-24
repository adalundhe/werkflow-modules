from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_endpoint_authorization import RedshiftEndpointAuthorization


class RedshiftDescribeEndpointAuthorizationResponse(BaseModel):
    EndpointAuthorizationList: list[RedshiftEndpointAuthorization] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

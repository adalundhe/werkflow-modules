from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_endpoint_access import RedshiftEndpointAccess


class RedshiftDescribeEndpointAccessResponse(BaseModel):
    EndpointAccessList: list[RedshiftEndpointAccess] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

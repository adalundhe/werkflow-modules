from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .glue_get_connections_filter import GlueGetConnectionsFilter


class GlueGetConnectionsRequest(BaseModel):
    CatalogId: StrictStr | None = None
    Filter: GlueGetConnectionsFilter | None = None
    HidePassword: StrictBool | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None

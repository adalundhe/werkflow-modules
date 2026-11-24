from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class AppSyncStartDataSourceIntrospectionResponse(BaseModel):
    introspectionId: StrictStr | None = None
    introspectionStatus: StrictStr | None = None
    introspectionStatusDetail: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

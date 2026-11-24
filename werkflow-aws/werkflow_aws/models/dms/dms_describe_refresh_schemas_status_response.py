from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_refresh_schemas_status import DMSRefreshSchemasStatus


class DMSDescribeRefreshSchemasStatusResponse(BaseModel):
    RefreshSchemasStatus: DMSRefreshSchemasStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None

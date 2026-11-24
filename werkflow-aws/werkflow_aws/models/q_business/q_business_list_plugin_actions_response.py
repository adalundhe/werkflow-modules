from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_action_summary import QBusinessActionSummary


class QBusinessListPluginActionsResponse(BaseModel):
    nextToken: StrictStr | None = None
    items: list[QBusinessActionSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None

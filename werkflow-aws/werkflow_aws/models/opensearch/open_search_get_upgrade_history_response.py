from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_upgrade_history import OpenSearchUpgradeHistory


class OpenSearchGetUpgradeHistoryResponse(BaseModel):
    UpgradeHistories: list[OpenSearchUpgradeHistory] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

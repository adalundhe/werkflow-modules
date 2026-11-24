from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_ops_item_event_summary import SSMOpsItemEventSummary


class SSMListOpsItemEventsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Summaries: list[SSMOpsItemEventSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None

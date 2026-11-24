from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_ops_item_event_filter import SSMOpsItemEventFilter


class SSMListOpsItemEventsRequest(BaseModel):
    Filters: list[SSMOpsItemEventFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None

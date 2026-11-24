from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_ops_item_related_item_summary import SSMOpsItemRelatedItemSummary


class SSMListOpsItemRelatedItemsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Summaries: list[SSMOpsItemRelatedItemSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None

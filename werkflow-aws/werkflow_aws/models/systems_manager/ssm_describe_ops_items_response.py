from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_ops_item_summary import SSMOpsItemSummary


class SSMDescribeOpsItemsResponse(BaseModel):
    NextToken: StrictStr | None = None
    OpsItemSummaries: list[SSMOpsItemSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None

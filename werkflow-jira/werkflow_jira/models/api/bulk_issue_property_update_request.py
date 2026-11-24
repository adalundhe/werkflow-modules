from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .issue_filter_for_bulk_property_set import IssueFilterForBulkPropertySet


class BulkIssuePropertyUpdateRequest(BaseModel):
    expression: StrictStr | None = None
    filter: IssueFilterForBulkPropertySet | None = None
    value: Any = None

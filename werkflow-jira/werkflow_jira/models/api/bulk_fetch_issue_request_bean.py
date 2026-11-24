from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BulkFetchIssueRequestBean(BaseModel):
    expand: list[StrictStr] | None = None
    fields: list[StrictStr] | None = None
    fieldsByKeys: StrictBool | None = None
    issueIdsOrKeys: list[StrictStr] | None = None
    properties: list[StrictStr] | None = None

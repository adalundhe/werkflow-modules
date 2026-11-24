from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .issue_bulk_edit_field import IssueBulkEditField


class BulkEditGetFields(BaseModel):
    endingBefore: StrictStr | None = None
    fields: list[IssueBulkEditField] | None = None
    startingAfter: StrictStr | None = None

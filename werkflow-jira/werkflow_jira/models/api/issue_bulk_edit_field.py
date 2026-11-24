from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .issue_bulk_operations_field_option import IssueBulkOperationsFieldOption


class IssueBulkEditField(BaseModel):
    description: StrictStr | None = None
    fieldOptions: list[IssueBulkOperationsFieldOption] | None = None
    id: StrictStr | None = None
    isRequired: StrictBool | None = None
    multiSelectFieldOptions: list[StrictStr] | None = None
    name: StrictStr | None = None
    searchUrl: StrictStr | None = None
    type: StrictStr | None = None
    unavailableMessage: StrictStr | None = None

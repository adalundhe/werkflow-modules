from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr

if TYPE_CHECKING:
    from .custom_field_context_default_value import CustomFieldContextDefaultValue


class IssueTypeDefaultValueUpdate(BaseModel):
    contextId: StrictInt | None = None
    isAnyIssueType: StrictBool | None = None
    issueTypeId: StrictStr | None = None
    operation: StrictStr | None = None
    value: CustomFieldContextDefaultValue | None = None

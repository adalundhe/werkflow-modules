from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictBool, StrictStr

if TYPE_CHECKING:
    from .custom_field_context_default_value import CustomFieldContextDefaultValue


class IssueTypeDefaultValue(BaseModel):
    isAnyIssueType: StrictBool | None = None
    issueTypeId: StrictStr | None = None
    value: CustomFieldContextDefaultValue | None = None

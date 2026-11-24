from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictBool, StrictStr

if TYPE_CHECKING:
    from .custom_field_context_default_value import CustomFieldContextDefaultValue


class AddIssueTypesToContext(BaseModel):
    defaultValue: CustomFieldContextDefaultValue | None = None
    isAnyIssueType: StrictBool | None = None
    issueTypeIds: list[StrictStr] | None = None

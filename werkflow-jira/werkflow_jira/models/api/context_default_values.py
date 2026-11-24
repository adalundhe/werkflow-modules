from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .issue_type_default_value import IssueTypeDefaultValue


class ContextDefaultValues(BaseModel):
    contextId: StrictInt | None = None
    defaultValues: list[IssueTypeDefaultValue] | None = None

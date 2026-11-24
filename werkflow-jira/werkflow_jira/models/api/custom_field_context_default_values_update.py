from __future__ import annotations
from pydantic import BaseModel
from .issue_type_default_value_update import IssueTypeDefaultValueUpdate


class CustomFieldContextDefaultValuesUpdate(BaseModel):
    defaultValues: list[IssueTypeDefaultValueUpdate] | None = None

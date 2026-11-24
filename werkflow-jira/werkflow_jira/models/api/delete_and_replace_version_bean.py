from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .custom_field_replacement import CustomFieldReplacement


class DeleteAndReplaceVersionBean(BaseModel):
    customFieldReplacementList: list[CustomFieldReplacement] | None = None
    moveAffectedIssuesTo: StrictInt | None = None
    moveFixIssuesTo: StrictInt | None = None

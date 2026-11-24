from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .field_metadata import FieldMetadata


class IssueUpdateMetadata(BaseModel):
    fields: dict[StrictStr, FieldMetadata] | None = None

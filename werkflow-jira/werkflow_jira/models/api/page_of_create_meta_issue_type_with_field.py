from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictInt
from .field_create_metadata import FieldCreateMetadata


class PageOfCreateMetaIssueTypeWithField(BaseModel):
    model_config = ConfigDict(extra="allow")

    fields: list[FieldCreateMetadata] | None = None
    maxResults: StrictInt | None = None
    results: list[FieldCreateMetadata] | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .field_create_metadata import FieldCreateMetadata


class PaginatedResponseFieldCreateMetadata(BaseModel):
    maxResults: StrictInt | None = None
    results: list[FieldCreateMetadata] | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None

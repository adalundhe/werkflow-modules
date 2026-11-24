from __future__ import annotations
from pydantic import BaseModel
from .field_scheme_to_fields_partial_failure import FieldSchemeToFieldsPartialFailure


class FieldSchemeToFieldsResponse(BaseModel):
    results: list[FieldSchemeToFieldsPartialFailure] | None = None

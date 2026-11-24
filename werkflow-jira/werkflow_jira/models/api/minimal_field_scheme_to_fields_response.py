from __future__ import annotations
from pydantic import BaseModel
from .minimal_field_scheme_to_fields_partial_failure import MinimalFieldSchemeToFieldsPartialFailure


class MinimalFieldSchemeToFieldsResponse(BaseModel):
    results: list[MinimalFieldSchemeToFieldsPartialFailure] | None = None

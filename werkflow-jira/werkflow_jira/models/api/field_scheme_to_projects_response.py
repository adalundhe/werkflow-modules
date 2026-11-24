from __future__ import annotations
from pydantic import BaseModel
from .field_scheme_to_projects_partial_failure import FieldSchemeToProjectsPartialFailure


class FieldSchemeToProjectsResponse(BaseModel):
    results: list[FieldSchemeToProjectsPartialFailure] | None = None

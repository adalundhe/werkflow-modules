from __future__ import annotations
from pydantic import BaseModel, StrictInt


class FieldSchemeToProjectsRequest(BaseModel):
    projectIds: list[StrictInt] | None = None

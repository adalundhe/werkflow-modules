from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class FieldLayoutConfiguration(BaseModel):
    field: StrictBool | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
    required: StrictBool | None = None

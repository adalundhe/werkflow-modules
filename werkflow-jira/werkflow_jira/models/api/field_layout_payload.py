from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .field_layout_configuration import FieldLayoutConfiguration
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class FieldLayoutPayload(BaseModel):
    configuration: list[FieldLayoutConfiguration] | None = None
    description: StrictStr | None = None
    name: StrictStr | None = None
    pcri: ProjectCreateResourceIdentifier | None = None

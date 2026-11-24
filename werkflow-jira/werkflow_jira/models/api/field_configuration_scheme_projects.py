from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .field_configuration_scheme import FieldConfigurationScheme


class FieldConfigurationSchemeProjects(BaseModel):
    fieldConfigurationScheme: FieldConfigurationScheme | None = None
    projectIds: list[StrictStr] | None = None

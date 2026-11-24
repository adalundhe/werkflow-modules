from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_parameter_definition_schema import CloudFrontParameterDefinitionSchema


class CloudFrontParameterDefinition(BaseModel):
    Name: StrictStr | None = None
    Definition: CloudFrontParameterDefinitionSchema | None = None

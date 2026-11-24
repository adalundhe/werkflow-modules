from __future__ import annotations
from pydantic import BaseModel
from .cloud_front_parameter_definition import CloudFrontParameterDefinition


class CloudFrontTenantConfig(BaseModel):
    ParameterDefinitions: list[CloudFrontParameterDefinition] | None = None

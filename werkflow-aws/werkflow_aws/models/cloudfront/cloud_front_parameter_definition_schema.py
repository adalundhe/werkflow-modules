from __future__ import annotations
from pydantic import BaseModel
from .cloud_front_string_schema_config import CloudFrontStringSchemaConfig


class CloudFrontParameterDefinitionSchema(BaseModel):
    StringSchema: CloudFrontStringSchemaConfig | None = None

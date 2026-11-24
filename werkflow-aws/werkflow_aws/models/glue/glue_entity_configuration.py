from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_field_definition import GlueFieldDefinition
from .glue_source_configuration import GlueSourceConfiguration


class GlueEntityConfiguration(BaseModel):
    SourceConfiguration: GlueSourceConfiguration | None = None
    Schema: dict[StrictStr, GlueFieldDefinition] | None = None

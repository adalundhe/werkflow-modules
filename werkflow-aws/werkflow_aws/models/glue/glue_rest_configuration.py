from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_entity_configuration import GlueEntityConfiguration
from .glue_source_configuration import GlueSourceConfiguration


class GlueRestConfiguration(BaseModel):
    GlobalSourceConfiguration: GlueSourceConfiguration | None = None
    ValidationEndpointConfiguration: GlueSourceConfiguration | None = None
    EntityConfigurations: dict[StrictStr, GlueEntityConfiguration] | None = None

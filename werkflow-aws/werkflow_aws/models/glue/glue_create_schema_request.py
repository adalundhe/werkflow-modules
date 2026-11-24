from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .glue_registry_id import GlueRegistryId


class GlueCreateSchemaRequest(BaseModel):
    SchemaName: StrictStr
    DataFormat: Literal['AVRO', 'JSON', 'PROTOBUF']
    RegistryId: GlueRegistryId | None = None
    Compatibility: Literal['NONE', 'DISABLED', 'BACKWARD', 'BACKWARD_ALL', 'FORWARD', 'FORWARD_ALL', 'FULL', 'FULL_ALL'] | None = None
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    SchemaDefinition: StrictStr | None = None

from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GlueCheckSchemaVersionValidityRequest(BaseModel):
    DataFormat: Literal['AVRO', 'JSON', 'PROTOBUF']
    SchemaDefinition: StrictStr

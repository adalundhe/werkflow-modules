from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_schema import GlueSchema
from .glue_snowflake_node_data import GlueSnowflakeNodeData


class GlueSnowflakeSource(BaseModel):
    Name: StrictStr | None = None
    Data: GlueSnowflakeNodeData | None = None
    OutputSchemas: list[GlueSchema] | None = None

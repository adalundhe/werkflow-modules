from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_snowflake_node_data import GlueSnowflakeNodeData


class GlueSnowflakeTarget(BaseModel):
    Name: StrictStr | None = None
    Data: GlueSnowflakeNodeData | None = None
    Inputs: list[StrictStr] | None = None

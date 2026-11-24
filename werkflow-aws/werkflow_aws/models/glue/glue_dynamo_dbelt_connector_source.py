from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_ddbelt_connection_options import GlueDDBELTConnectionOptions
from .glue_schema import GlueSchema


class GlueDynamoDBELTConnectorSource(BaseModel):
    Name: StrictStr | None = None
    ConnectionOptions: GlueDDBELTConnectionOptions | None = None
    OutputSchemas: list[GlueSchema] | None = None

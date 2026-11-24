from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_amazon_redshift_node_data import GlueAmazonRedshiftNodeData


class GlueAmazonRedshiftSource(BaseModel):
    Name: StrictStr | None = None
    Data: GlueAmazonRedshiftNodeData | None = None

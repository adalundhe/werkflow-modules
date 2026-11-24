from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .redshift_reserved_node import RedshiftReservedNode
from .redshift_reserved_node_offering import RedshiftReservedNodeOffering


class RedshiftReservedNodeConfigurationOption(BaseModel):
    SourceReservedNode: RedshiftReservedNode | None = None
    TargetReservedNodeCount: StrictInt | None = None
    TargetReservedNodeOffering: RedshiftReservedNodeOffering | None = None

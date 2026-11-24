from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftGetReservedNodeExchangeConfigurationOptionsRequest(BaseModel):
    ActionType: Literal['restore-cluster', 'resize-cluster']
    ClusterIdentifier: StrictStr | None = None
    SnapshotIdentifier: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None

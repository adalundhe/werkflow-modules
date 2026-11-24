from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .redshift_node_configuration_options_filter import RedshiftNodeConfigurationOptionsFilter


class RedshiftDescribeNodeConfigurationOptionsRequest(BaseModel):
    ActionType: Literal['restore-cluster', 'recommend-node-config', 'resize-cluster']
    ClusterIdentifier: StrictStr | None = None
    SnapshotIdentifier: StrictStr | None = None
    SnapshotArn: StrictStr | None = None
    OwnerAccount: StrictStr | None = None
    Filters: list[RedshiftNodeConfigurationOptionsFilter] | None = None
    Marker: StrictStr | None = None
    MaxRecords: StrictInt | None = None

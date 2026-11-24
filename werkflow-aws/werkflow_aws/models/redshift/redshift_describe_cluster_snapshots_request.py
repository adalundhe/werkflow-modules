from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .redshift_snapshot_sorting_entity import RedshiftSnapshotSortingEntity


class RedshiftDescribeClusterSnapshotsRequest(BaseModel):
    ClusterIdentifier: StrictStr | None = None
    SnapshotIdentifier: StrictStr | None = None
    SnapshotArn: StrictStr | None = None
    SnapshotType: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    OwnerAccount: StrictStr | None = None
    TagKeys: list[StrictStr] | None = None
    TagValues: list[StrictStr] | None = None
    ClusterExists: StrictBool | None = None
    SortingEntities: list[RedshiftSnapshotSortingEntity] | None = None

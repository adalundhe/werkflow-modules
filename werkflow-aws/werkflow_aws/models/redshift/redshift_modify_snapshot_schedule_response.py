from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .redshift_cluster_associated_to_schedule import RedshiftClusterAssociatedToSchedule
from .redshift_tag import RedshiftTag


class RedshiftModifySnapshotScheduleResponse(BaseModel):
    ScheduleDefinitions: list[StrictStr] | None = None
    ScheduleIdentifier: StrictStr | None = None
    ScheduleDescription: StrictStr | None = None
    Tags: list[RedshiftTag] | None = None
    NextInvocations: list[datetime.datetime | StrictStr] | None = None
    AssociatedClusterCount: StrictInt | None = None
    AssociatedClusters: list[RedshiftClusterAssociatedToSchedule] | None = None
    ResponseMetadata: dict[str, Any] | None = None

from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .redshift_revision_target import RedshiftRevisionTarget


class RedshiftClusterDbRevision(BaseModel):
    ClusterIdentifier: StrictStr | None = None
    CurrentDatabaseRevision: StrictStr | None = None
    DatabaseRevisionReleaseDate: datetime.datetime | StrictStr | None = None
    RevisionTargets: list[RedshiftRevisionTarget] | None = None

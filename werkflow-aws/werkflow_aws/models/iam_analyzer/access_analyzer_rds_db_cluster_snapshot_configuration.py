from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .access_analyzer_rds_db_cluster_snapshot_attribute_value import AccessAnalyzerRdsDbClusterSnapshotAttributeValue


class AccessAnalyzerRdsDbClusterSnapshotConfiguration(BaseModel):
    attributes: dict[StrictStr, AccessAnalyzerRdsDbClusterSnapshotAttributeValue] | None = None
    kmsKeyId: StrictStr | None = None

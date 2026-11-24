from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .access_analyzer_rds_db_snapshot_attribute_value import AccessAnalyzerRdsDbSnapshotAttributeValue


class AccessAnalyzerRdsDbSnapshotConfiguration(BaseModel):
    attributes: dict[StrictStr, AccessAnalyzerRdsDbSnapshotAttributeValue] | None = None
    kmsKeyId: StrictStr | None = None

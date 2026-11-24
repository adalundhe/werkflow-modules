from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .document_db_tag import DocumentDBTag


class DocumentDBCreateDBInstanceRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    DBInstanceClass: StrictStr
    Engine: StrictStr
    DBClusterIdentifier: StrictStr
    AvailabilityZone: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    Tags: list[DocumentDBTag] | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    PromotionTier: StrictInt | None = None
    EnablePerformanceInsights: StrictBool | None = None
    PerformanceInsightsKMSKeyId: StrictStr | None = None
    CACertificateIdentifier: StrictStr | None = None

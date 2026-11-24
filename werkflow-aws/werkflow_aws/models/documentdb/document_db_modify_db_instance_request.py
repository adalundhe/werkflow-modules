from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DocumentDBModifyDBInstanceRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    DBInstanceClass: StrictStr | None = None
    ApplyImmediately: StrictBool | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    NewDBInstanceIdentifier: StrictStr | None = None
    CACertificateIdentifier: StrictStr | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    PromotionTier: StrictInt | None = None
    EnablePerformanceInsights: StrictBool | None = None
    PerformanceInsightsKMSKeyId: StrictStr | None = None
    CertificateRotationRestart: StrictBool | None = None

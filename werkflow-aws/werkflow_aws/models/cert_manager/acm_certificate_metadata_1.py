from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class AcmCertificateMetadata(BaseModel):
    CreatedAt: datetime.datetime | StrictStr | None = None
    Exported: StrictBool | None = None
    ImportedAt: datetime.datetime | StrictStr | None = None
    InUse: StrictBool | None = None
    IssuedAt: datetime.datetime | StrictStr | None = None
    RenewalEligibility: StrictStr | None = None
    RevokedAt: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    RenewalStatus: StrictStr | None = None
    Type: StrictStr | None = None
    ExportOption: StrictStr | None = None
    ManagedBy: StrictStr | None = None
    ValidationMethod: StrictStr | None = None
    CertificateKeyPairOrigin: StrictStr | None = None
    AcmeEndpointArn: StrictStr | None = None
    AcmeAccountId: StrictStr | None = None
    CertificateUsage: StrictStr | None = None
    RootHierarchyType: StrictStr | None = None

from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class ACMCertificateSummary(BaseModel):
    CertificateArn: StrictStr | None = None
    DomainName: StrictStr | None = None
    SubjectAlternativeNameSummaries: list[StrictStr] | None = None
    HasAdditionalSubjectAlternativeNames: StrictBool | None = None
    Status: StrictStr | None = None
    Type: StrictStr | None = None
    KeyAlgorithm: StrictStr | None = None
    KeyUsages: list[StrictStr] | None = None
    ExtendedKeyUsages: list[StrictStr] | None = None
    ExportOption: StrictStr | None = None
    InUse: StrictBool | None = None
    Exported: StrictBool | None = None
    RenewalEligibility: StrictStr | None = None
    NotBefore: datetime.datetime | StrictStr | None = None
    NotAfter: datetime.datetime | StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    IssuedAt: datetime.datetime | StrictStr | None = None
    ImportedAt: datetime.datetime | StrictStr | None = None
    RevokedAt: datetime.datetime | StrictStr | None = None
    ManagedBy: StrictStr | None = None
    CertificateKeyPairOrigin: StrictStr | None = None
    CertificateUsage: StrictStr | None = None
    RootHierarchyType: StrictStr | None = None

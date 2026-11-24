from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class AcmCertificateMetadataFilter(BaseModel):
    Status: Literal['PENDING_VALIDATION', 'ISSUED', 'INACTIVE', 'EXPIRED', 'VALIDATION_TIMED_OUT', 'REVOKED', 'FAILED'] | None = None
    RenewalStatus: Literal['PENDING_AUTO_RENEWAL', 'PENDING_VALIDATION', 'SUCCESS', 'FAILED'] | None = None
    Type: Literal['IMPORTED', 'AMAZON_ISSUED', 'PRIVATE'] | None = None
    InUse: StrictBool | None = None
    Exported: StrictBool | None = None
    ExportOption: Literal['ENABLED', 'DISABLED'] | None = None
    ManagedBy: Literal['CLOUDFRONT'] | None = None
    ValidationMethod: Literal['EMAIL', 'DNS', 'HTTP'] | None = None
    CertificateKeyPairOrigin: Literal['AWS_MANAGED', 'ACME', 'CUSTOMER_PROVIDED'] | None = None
    AcmeEndpointArn: StrictStr | None = None
    AcmeAccountId: StrictStr | None = None
    RootHierarchyType: Literal['N2_AMAZON_MANAGED', 'N2_SFG2_AMAZON_MANAGED'] | None = None

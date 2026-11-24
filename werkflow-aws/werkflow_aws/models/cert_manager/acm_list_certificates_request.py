from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .acm_filters import ACMFilters


class ACMListCertificatesRequest(BaseModel):
    CertificateStatuses: list[Literal['PENDING_VALIDATION', 'ISSUED', 'INACTIVE', 'EXPIRED', 'VALIDATION_TIMED_OUT', 'REVOKED', 'FAILED']] | None = None
    CertificateKeyPairOrigins: list[Literal['AWS_MANAGED', 'ACME', 'CUSTOMER_PROVIDED']] | None = None
    RootHierarchyTypes: list[Literal['N2_AMAZON_MANAGED', 'N2_SFG2_AMAZON_MANAGED']] | None = None
    Includes: ACMFilters | None = None
    NextToken: StrictStr | None = None
    MaxItems: StrictInt | None = None
    SortBy: Literal['CREATED_AT'] | None = None
    SortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None

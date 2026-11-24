from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .acm_certificate_filter_statement import ACMCertificateFilterStatement


class ACMSearchCertificatesRequest(BaseModel):
    FilterStatement: ACMCertificateFilterStatement | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    SortBy: Literal['CREATED_AT', 'NOT_AFTER', 'STATUS', 'RENEWAL_STATUS', 'EXPORTED', 'IN_USE', 'NOT_BEFORE', 'KEY_ALGORITHM', 'TYPE', 'CERTIFICATE_ARN', 'COMMON_NAME', 'REVOKED_AT', 'RENEWAL_ELIGIBILITY', 'ISSUED_AT', 'MANAGED_BY', 'EXPORT_OPTION', 'VALIDATION_METHOD', 'IMPORTED_AT', 'ACME_ENDPOINT_ARN', 'ACME_ACCOUNT_ID', 'CERTIFICATE_KEY_PAIR_ORIGIN'] | None = None
    SortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None

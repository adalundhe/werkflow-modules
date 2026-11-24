from __future__ import annotations
from pydantic import BaseModel
from .acm_dns_prevalidation_details import ACMDnsPrevalidationDetails


class ACMPrevalidationDetails(BaseModel):
    DnsPrevalidation: ACMDnsPrevalidationDetails | None = None

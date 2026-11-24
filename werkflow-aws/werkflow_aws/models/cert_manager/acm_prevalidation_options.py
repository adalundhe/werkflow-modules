from __future__ import annotations
from pydantic import BaseModel
from .acm_dns_prevalidation_options import ACMDnsPrevalidationOptions


class ACMPrevalidationOptions(BaseModel):
    DnsPrevalidation: ACMDnsPrevalidationOptions | None = None

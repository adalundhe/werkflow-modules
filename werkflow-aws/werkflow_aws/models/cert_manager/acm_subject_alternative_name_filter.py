from __future__ import annotations
from pydantic import BaseModel
from .acm_dns_name_filter import ACMDnsNameFilter


class ACMSubjectAlternativeNameFilter(BaseModel):
    DnsName: ACMDnsNameFilter | None = None

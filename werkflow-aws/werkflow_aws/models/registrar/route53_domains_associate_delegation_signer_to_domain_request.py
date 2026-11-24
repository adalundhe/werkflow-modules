from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_domains_dnssec_signing_attributes import Route53DomainsDnssecSigningAttributes


class Route53DomainsAssociateDelegationSignerToDomainRequest(BaseModel):
    DomainName: StrictStr
    SigningAttributes: Route53DomainsDnssecSigningAttributes

from __future__ import annotations
from pydantic import BaseModel
from .acm_resource_record import ACMResourceRecord


class ACMDnsValidationChallenge(BaseModel):
    ResourceRecord: ACMResourceRecord | None = None

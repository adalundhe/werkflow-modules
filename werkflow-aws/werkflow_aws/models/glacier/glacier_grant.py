from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glacier_grantee import GlacierGrantee


class GlacierGrant(BaseModel):
    Grantee: GlacierGrantee | None = None
    Permission: StrictStr | None = None

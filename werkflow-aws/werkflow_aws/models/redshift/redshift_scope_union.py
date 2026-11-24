from __future__ import annotations
from pydantic import BaseModel
from .redshift_connect import RedshiftConnect


class RedshiftScopeUnion(BaseModel):
    Connect: RedshiftConnect | None = None

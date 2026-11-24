from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rdsdb_proxy import RDSDBProxy


class RDSCreateDBProxyResponse(BaseModel):
    DBProxy: RDSDBProxy | None = None
    ResponseMetadata: dict[str, Any] | None = None

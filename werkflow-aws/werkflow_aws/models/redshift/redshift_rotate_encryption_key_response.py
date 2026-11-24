from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_cluster import RedshiftCluster


class RedshiftRotateEncryptionKeyResponse(BaseModel):
    Cluster: RedshiftCluster | None = None
    ResponseMetadata: dict[str, Any] | None = None

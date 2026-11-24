from __future__ import annotations
from pydantic import BaseModel
from .redshift_read_write_access import RedshiftReadWriteAccess


class RedshiftS3AccessGrantsScopeUnion(BaseModel):
    ReadWriteAccess: RedshiftReadWriteAccess | None = None

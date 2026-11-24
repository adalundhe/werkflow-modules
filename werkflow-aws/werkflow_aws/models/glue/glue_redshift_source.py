from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueRedshiftSource(BaseModel):
    Name: StrictStr | None = None
    Database: StrictStr | None = None
    Table: StrictStr | None = None
    RedshiftTmpDir: StrictStr | None = None
    TmpDirIAMRole: StrictStr | None = None

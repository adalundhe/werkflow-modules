from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_upsert_redshift_target_options import GlueUpsertRedshiftTargetOptions


class GlueRedshiftTarget(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    Database: StrictStr | None = None
    Table: StrictStr | None = None
    RedshiftTmpDir: StrictStr | None = None
    TmpDirIAMRole: StrictStr | None = None
    UpsertRedshiftOptions: GlueUpsertRedshiftTargetOptions | None = None

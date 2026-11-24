from __future__ import annotations
from pydantic import BaseModel
from .redshift_lake_formation_scope_union import RedshiftLakeFormationScopeUnion
from .redshift_s3_access_grants_scope_union import RedshiftS3AccessGrantsScopeUnion
from .redshift_scope_union import RedshiftScopeUnion


class RedshiftServiceIntegrationsUnion(BaseModel):
    LakeFormation: list[RedshiftLakeFormationScopeUnion] | None = None
    S3AccessGrants: list[RedshiftS3AccessGrantsScopeUnion] | None = None
    Redshift: list[RedshiftScopeUnion] | None = None

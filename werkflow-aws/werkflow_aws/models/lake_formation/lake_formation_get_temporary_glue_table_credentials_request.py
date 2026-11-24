from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .lake_formation_audit_context import LakeFormationAuditContext
from .lake_formation_query_session_context import LakeFormationQuerySessionContext


class LakeFormationGetTemporaryGlueTableCredentialsRequest(BaseModel):
    TableArn: StrictStr
    Permissions: list[Literal['ALL', 'SELECT', 'ALTER', 'DROP', 'DELETE', 'INSERT', 'DESCRIBE', 'CREATE_DATABASE', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'CREATE_LF_TAG', 'ASSOCIATE', 'GRANT_WITH_LF_TAG_EXPRESSION', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_CATALOG', 'SUPER_USER', 'EXECUTE']] | None = None
    DurationSeconds: StrictInt | None = None
    AuditContext: LakeFormationAuditContext | None = None
    SupportedPermissionTypes: list[Literal['COLUMN_PERMISSION', 'CELL_FILTER_PERMISSION', 'NESTED_PERMISSION', 'NESTED_CELL_PERMISSION']] | None = None
    S3Path: StrictStr | None = None
    QuerySessionContext: LakeFormationQuerySessionContext | None = None

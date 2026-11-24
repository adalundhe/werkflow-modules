from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .glue_audit_context import GlueAuditContext
from .glue_query_session_context import GlueQuerySessionContext
from .glue_supported_dialect import GlueSupportedDialect


class GlueGetUnfilteredTableMetadataRequest(BaseModel):
    CatalogId: StrictStr
    DatabaseName: StrictStr
    Name: StrictStr
    SupportedPermissionTypes: list[Literal['COLUMN_PERMISSION', 'CELL_FILTER_PERMISSION', 'NESTED_PERMISSION', 'NESTED_CELL_PERMISSION']]
    Region: StrictStr | None = None
    AuditContext: GlueAuditContext | None = None
    ParentResourceArn: StrictStr | None = None
    RootResourceArn: StrictStr | None = None
    SupportedDialect: GlueSupportedDialect | None = None
    Permissions: list[Literal['ALL', 'SELECT', 'ALTER', 'DROP', 'DELETE', 'INSERT', 'CREATE_DATABASE', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS']] | None = None
    QuerySessionContext: GlueQuerySessionContext | None = None

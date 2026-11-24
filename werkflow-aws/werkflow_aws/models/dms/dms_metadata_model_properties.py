from __future__ import annotations
from pydantic import BaseModel
from .dms_statement_properties import DMSStatementProperties


class DMSMetadataModelProperties(BaseModel):
    StatementProperties: DMSStatementProperties | None = None

from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EventBridgeRedshiftDataParameters(BaseModel):
    SecretManagerArn: StrictStr | None = None
    Database: StrictStr | None = None
    DbUser: StrictStr | None = None
    Sql: StrictStr | None = None
    StatementName: StrictStr | None = None
    WithEvent: StrictBool | None = None
    Sqls: list[StrictStr] | None = None

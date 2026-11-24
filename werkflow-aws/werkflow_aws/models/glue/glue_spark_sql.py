from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_schema import GlueSchema
from .glue_sql_alias import GlueSqlAlias


class GlueSparkSQL(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    SqlQuery: StrictStr | None = None
    SqlAliases: list[GlueSqlAlias] | None = None
    OutputSchemas: list[GlueSchema] | None = None

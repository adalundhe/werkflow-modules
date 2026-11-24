from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_option import GlueOption


class GlueSnowflakeNodeData(BaseModel):
    SourceType: StrictStr | None = None
    Connection: GlueOption | None = None
    Schema: StrictStr | None = None
    Table: StrictStr | None = None
    Database: StrictStr | None = None
    TempDir: StrictStr | None = None
    IamRole: GlueOption | None = None
    AdditionalOptions: dict[StrictStr, StrictStr] | None = None
    SampleQuery: StrictStr | None = None
    PreAction: StrictStr | None = None
    PostAction: StrictStr | None = None
    Action: StrictStr | None = None
    Upsert: StrictBool | None = None
    MergeAction: StrictStr | None = None
    MergeWhenMatched: StrictStr | None = None
    MergeWhenNotMatched: StrictStr | None = None
    MergeClause: StrictStr | None = None
    StagingTable: StrictStr | None = None
    SelectedColumns: list[GlueOption] | None = None
    AutoPushdown: StrictBool | None = None
    TableSchema: list[GlueOption] | None = None

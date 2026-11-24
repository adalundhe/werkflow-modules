from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_amazon_redshift_advanced_option import GlueAmazonRedshiftAdvancedOption
from .glue_option import GlueOption


class GlueAmazonRedshiftNodeData(BaseModel):
    AccessType: StrictStr | None = None
    SourceType: StrictStr | None = None
    Connection: GlueOption | None = None
    Schema: GlueOption | None = None
    Table: GlueOption | None = None
    CatalogDatabase: GlueOption | None = None
    CatalogTable: GlueOption | None = None
    CatalogRedshiftSchema: StrictStr | None = None
    CatalogRedshiftTable: StrictStr | None = None
    TempDir: StrictStr | None = None
    IamRole: GlueOption | None = None
    AdvancedOptions: list[GlueAmazonRedshiftAdvancedOption] | None = None
    SampleQuery: StrictStr | None = None
    PreAction: StrictStr | None = None
    PostAction: StrictStr | None = None
    Action: StrictStr | None = None
    TablePrefix: StrictStr | None = None
    Upsert: StrictBool | None = None
    MergeAction: StrictStr | None = None
    MergeWhenMatched: StrictStr | None = None
    MergeWhenNotMatched: StrictStr | None = None
    MergeClause: StrictStr | None = None
    CrawlerConnection: StrictStr | None = None
    TableSchema: list[GlueOption] | None = None
    StagingTable: StrictStr | None = None
    SelectedColumns: list[GlueOption] | None = None

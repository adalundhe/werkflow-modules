from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_crawler_targets import GlueCrawlerTargets
from .glue_lake_formation_configuration import GlueLakeFormationConfiguration
from .glue_lineage_configuration import GlueLineageConfiguration
from .glue_recrawl_policy import GlueRecrawlPolicy
from .glue_schema_change_policy import GlueSchemaChangePolicy


class GlueCreateCrawlerRequest(BaseModel):
    Name: StrictStr
    Role: StrictStr
    Targets: GlueCrawlerTargets
    DatabaseName: StrictStr | None = None
    Description: StrictStr | None = None
    Schedule: StrictStr | None = None
    Classifiers: list[StrictStr] | None = None
    TablePrefix: StrictStr | None = None
    SchemaChangePolicy: GlueSchemaChangePolicy | None = None
    RecrawlPolicy: GlueRecrawlPolicy | None = None
    LineageConfiguration: GlueLineageConfiguration | None = None
    LakeFormationConfiguration: GlueLakeFormationConfiguration | None = None
    Configuration: StrictStr | None = None
    CrawlerSecurityConfiguration: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    CatalogId: StrictStr | None = None

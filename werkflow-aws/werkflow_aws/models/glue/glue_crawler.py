from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_crawler_targets import GlueCrawlerTargets
from .glue_lake_formation_configuration import GlueLakeFormationConfiguration
from .glue_last_crawl_info import GlueLastCrawlInfo
from .glue_lineage_configuration import GlueLineageConfiguration
from .glue_recrawl_policy import GlueRecrawlPolicy
from .glue_schedule import GlueSchedule
from .glue_schema_change_policy import GlueSchemaChangePolicy


class GlueCrawler(BaseModel):
    Name: StrictStr | None = None
    Role: StrictStr | None = None
    Targets: GlueCrawlerTargets | None = None
    DatabaseName: StrictStr | None = None
    Description: StrictStr | None = None
    Classifiers: list[StrictStr] | None = None
    RecrawlPolicy: GlueRecrawlPolicy | None = None
    SchemaChangePolicy: GlueSchemaChangePolicy | None = None
    LineageConfiguration: GlueLineageConfiguration | None = None
    State: StrictStr | None = None
    TablePrefix: StrictStr | None = None
    Schedule: GlueSchedule | None = None
    CrawlElapsedTime: StrictInt | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdated: datetime.datetime | StrictStr | None = None
    LastCrawl: GlueLastCrawlInfo | None = None
    Version: StrictInt | None = None
    Configuration: StrictStr | None = None
    CrawlerSecurityConfiguration: StrictStr | None = None
    LakeFormationConfiguration: GlueLakeFormationConfiguration | None = None
    CatalogId: StrictStr | None = None

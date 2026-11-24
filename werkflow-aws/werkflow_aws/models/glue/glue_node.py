from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_crawler_node_details import GlueCrawlerNodeDetails
from .glue_job_node_details import GlueJobNodeDetails
from .glue_trigger_node_details import GlueTriggerNodeDetails


class GlueNode(BaseModel):
    Type: StrictStr | None = None
    Name: StrictStr | None = None
    UniqueId: StrictStr | None = None
    TriggerDetails: GlueTriggerNodeDetails | None = None
    JobDetails: GlueJobNodeDetails | None = None
    CrawlerDetails: GlueCrawlerNodeDetails | None = None

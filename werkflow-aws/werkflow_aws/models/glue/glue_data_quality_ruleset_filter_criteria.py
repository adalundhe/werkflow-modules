from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_data_quality_target_table import GlueDataQualityTargetTable


class GlueDataQualityRulesetFilterCriteria(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedBefore: datetime.datetime | StrictStr | None = None
    CreatedAfter: datetime.datetime | StrictStr | None = None
    LastModifiedBefore: datetime.datetime | StrictStr | None = None
    LastModifiedAfter: datetime.datetime | StrictStr | None = None
    TargetTable: GlueDataQualityTargetTable | None = None

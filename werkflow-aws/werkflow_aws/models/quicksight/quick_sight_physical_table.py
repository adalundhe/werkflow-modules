from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_custom_sql import QuickSightCustomSql
from .quick_sight_file_source import QuickSightFileSource
from .quick_sight_relational_table import QuickSightRelationalTable
from .quick_sight_s3_source import QuickSightS3Source
from .quick_sight_saa_s_table import QuickSightSaaSTable


class QuickSightPhysicalTable(BaseModel):
    RelationalTable: QuickSightRelationalTable | None = None
    CustomSql: QuickSightCustomSql | None = None
    S3Source: QuickSightS3Source | None = None
    SaaSTable: QuickSightSaaSTable | None = None
    FileSource: QuickSightFileSource | None = None

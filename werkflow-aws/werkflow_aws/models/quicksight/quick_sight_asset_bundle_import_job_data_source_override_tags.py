from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_tag import QuickSightTag


class QuickSightAssetBundleImportJobDataSourceOverrideTags(BaseModel):
    DataSourceIds: list[StrictStr] | None = None
    Tags: list[QuickSightTag] | None = None

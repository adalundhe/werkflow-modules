from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_event_info_map import RedshiftEventInfoMap


class RedshiftEventCategoriesMap(BaseModel):
    SourceType: StrictStr | None = None
    Events: list[RedshiftEventInfoMap] | None = None

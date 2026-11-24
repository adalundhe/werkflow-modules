from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .data_zone_relational_filter_configuration import DataZoneRelationalFilterConfiguration


class DataZoneGlueRunConfigurationInput(BaseModel):
    relationalFilterConfigurations: list[DataZoneRelationalFilterConfiguration]
    dataAccessRole: StrictStr | None = None
    autoImportDataQualityResult: StrictBool | None = None
    catalogName: StrictStr | None = None

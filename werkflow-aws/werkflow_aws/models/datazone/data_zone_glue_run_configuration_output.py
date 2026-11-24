from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .data_zone_relational_filter_configuration import DataZoneRelationalFilterConfiguration


class DataZoneGlueRunConfigurationOutput(BaseModel):
    accountId: StrictStr | None = None
    region: StrictStr | None = None
    dataAccessRole: StrictStr | None = None
    relationalFilterConfigurations: list[DataZoneRelationalFilterConfiguration] | None = None
    autoImportDataQualityResult: StrictBool | None = None
    catalogName: StrictStr | None = None

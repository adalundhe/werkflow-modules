from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .data_zone_data_source_configuration_input import DataZoneDataSourceConfigurationInput
from .data_zone_form_input import DataZoneFormInput
from .data_zone_recommendation_configuration import DataZoneRecommendationConfiguration
from .data_zone_schedule_configuration import DataZoneScheduleConfiguration


class DataZoneCreateDataSourceRequest(BaseModel):
    name: StrictStr
    domainIdentifier: StrictStr
    projectIdentifier: StrictStr
    type: StrictStr
    description: StrictStr | None = None
    environmentIdentifier: StrictStr | None = None
    connectionIdentifier: StrictStr | None = None
    configuration: DataZoneDataSourceConfigurationInput | None = None
    recommendation: DataZoneRecommendationConfiguration | None = None
    enableSetting: Literal['ENABLED', 'DISABLED'] | None = None
    schedule: DataZoneScheduleConfiguration | None = None
    publishOnImport: StrictBool | None = None
    assetFormsInput: list[DataZoneFormInput] | None = None
    clientToken: StrictStr | None = None

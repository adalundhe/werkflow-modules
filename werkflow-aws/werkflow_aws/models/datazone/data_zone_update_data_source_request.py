from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .data_zone_data_source_configuration_input import DataZoneDataSourceConfigurationInput
from .data_zone_form_input import DataZoneFormInput
from .data_zone_recommendation_configuration import DataZoneRecommendationConfiguration
from .data_zone_schedule_configuration import DataZoneScheduleConfiguration


class DataZoneUpdateDataSourceRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    name: StrictStr | None = None
    description: StrictStr | None = None
    enableSetting: Literal['ENABLED', 'DISABLED'] | None = None
    publishOnImport: StrictBool | None = None
    assetFormsInput: list[DataZoneFormInput] | None = None
    schedule: DataZoneScheduleConfiguration | None = None
    configuration: DataZoneDataSourceConfigurationInput | None = None
    recommendation: DataZoneRecommendationConfiguration | None = None
    retainPermissionsOnRevokeFailure: StrictBool | None = None

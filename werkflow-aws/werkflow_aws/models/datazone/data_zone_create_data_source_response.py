from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .data_zone_data_source_configuration_output import DataZoneDataSourceConfigurationOutput
from .data_zone_data_source_error_message import DataZoneDataSourceErrorMessage
from .data_zone_form_output import DataZoneFormOutput
from .data_zone_recommendation_configuration import DataZoneRecommendationConfiguration
from .data_zone_schedule_configuration import DataZoneScheduleConfiguration


class DataZoneCreateDataSourceResponse(BaseModel):
    id: StrictStr | None = None
    status: StrictStr | None = None
    type: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    domainId: StrictStr | None = None
    projectId: StrictStr | None = None
    environmentId: StrictStr | None = None
    connectionId: StrictStr | None = None
    configuration: DataZoneDataSourceConfigurationOutput | None = None
    recommendation: DataZoneRecommendationConfiguration | None = None
    enableSetting: StrictStr | None = None
    publishOnImport: StrictBool | None = None
    assetFormsOutput: list[DataZoneFormOutput] | None = None
    schedule: DataZoneScheduleConfiguration | None = None
    lastRunStatus: StrictStr | None = None
    lastRunAt: datetime.datetime | StrictStr | None = None
    lastRunErrorMessage: DataZoneDataSourceErrorMessage | None = None
    errorMessage: DataZoneDataSourceErrorMessage | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

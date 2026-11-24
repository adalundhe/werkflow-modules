from __future__ import annotations
from pydantic import BaseModel
from .data_zone_glue_run_configuration_input import DataZoneGlueRunConfigurationInput
from .data_zone_redshift_run_configuration_input import DataZoneRedshiftRunConfigurationInput
from .data_zone_sage_maker_run_configuration_input import DataZoneSageMakerRunConfigurationInput


class DataZoneDataSourceConfigurationInput(BaseModel):
    glueRunConfiguration: DataZoneGlueRunConfigurationInput | None = None
    redshiftRunConfiguration: DataZoneRedshiftRunConfigurationInput | None = None
    sageMakerRunConfiguration: DataZoneSageMakerRunConfigurationInput | None = None

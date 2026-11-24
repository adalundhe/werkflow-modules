from __future__ import annotations
from pydantic import BaseModel
from .data_zone_glue_run_configuration_output import DataZoneGlueRunConfigurationOutput
from .data_zone_redshift_run_configuration_output import DataZoneRedshiftRunConfigurationOutput
from .data_zone_sage_maker_run_configuration_output import DataZoneSageMakerRunConfigurationOutput


class DataZoneDataSourceConfigurationOutput(BaseModel):
    glueRunConfiguration: DataZoneGlueRunConfigurationOutput | None = None
    redshiftRunConfiguration: DataZoneRedshiftRunConfigurationOutput | None = None
    sageMakerRunConfiguration: DataZoneSageMakerRunConfigurationOutput | None = None

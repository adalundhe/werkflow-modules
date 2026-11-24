from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fis_experiment_report_configuration_data_sources import FISExperimentReportConfigurationDataSources
from .fis_experiment_report_configuration_outputs import FISExperimentReportConfigurationOutputs


class FISExperimentReportConfiguration(BaseModel):
    outputs: FISExperimentReportConfigurationOutputs | None = None
    dataSources: FISExperimentReportConfigurationDataSources | None = None
    preExperimentDuration: StrictStr | None = None
    postExperimentDuration: StrictStr | None = None

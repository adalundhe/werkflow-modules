from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fis_experiment_template_report_configuration_data_sources import FISExperimentTemplateReportConfigurationDataSources
from .fis_experiment_template_report_configuration_outputs import FISExperimentTemplateReportConfigurationOutputs


class FISExperimentTemplateReportConfiguration(BaseModel):
    outputs: FISExperimentTemplateReportConfigurationOutputs | None = None
    dataSources: FISExperimentTemplateReportConfigurationDataSources | None = None
    preExperimentDuration: StrictStr | None = None
    postExperimentDuration: StrictStr | None = None

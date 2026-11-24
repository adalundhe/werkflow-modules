from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fis_experiment_template_report_configuration_data_sources_input import FISExperimentTemplateReportConfigurationDataSourcesInput
from .fis_experiment_template_report_configuration_outputs_input import FISExperimentTemplateReportConfigurationOutputsInput


class FISUpdateExperimentTemplateReportConfigurationInput(BaseModel):
    outputs: FISExperimentTemplateReportConfigurationOutputsInput | None = None
    dataSources: FISExperimentTemplateReportConfigurationDataSourcesInput | None = None
    preExperimentDuration: StrictStr | None = None
    postExperimentDuration: StrictStr | None = None

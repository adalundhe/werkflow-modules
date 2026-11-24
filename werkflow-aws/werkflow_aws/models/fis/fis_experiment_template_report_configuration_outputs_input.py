from __future__ import annotations
from pydantic import BaseModel
from .fis_report_configuration_s3_output_input import FISReportConfigurationS3OutputInput


class FISExperimentTemplateReportConfigurationOutputsInput(BaseModel):
    s3Configuration: FISReportConfigurationS3OutputInput | None = None

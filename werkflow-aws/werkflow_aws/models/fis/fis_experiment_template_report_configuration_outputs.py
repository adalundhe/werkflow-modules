from __future__ import annotations
from pydantic import BaseModel
from .fis_report_configuration_s3_output import FISReportConfigurationS3Output


class FISExperimentTemplateReportConfigurationOutputs(BaseModel):
    s3Configuration: FISReportConfigurationS3Output | None = None

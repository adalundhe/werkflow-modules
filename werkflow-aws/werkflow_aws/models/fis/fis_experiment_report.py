from __future__ import annotations
from pydantic import BaseModel
from .fis_experiment_report_s3_report import FISExperimentReportS3Report
from .fis_experiment_report_state import FISExperimentReportState


class FISExperimentReport(BaseModel):
    state: FISExperimentReportState | None = None
    s3Reports: list[FISExperimentReportS3Report] | None = None

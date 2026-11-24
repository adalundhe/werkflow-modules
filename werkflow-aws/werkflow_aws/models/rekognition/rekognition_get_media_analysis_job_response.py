from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_media_analysis_input import RekognitionMediaAnalysisInput
from .rekognition_media_analysis_job_failure_details import RekognitionMediaAnalysisJobFailureDetails
from .rekognition_media_analysis_manifest_summary import RekognitionMediaAnalysisManifestSummary
from .rekognition_media_analysis_operations_config import RekognitionMediaAnalysisOperationsConfig
from .rekognition_media_analysis_output_config import RekognitionMediaAnalysisOutputConfig
from .rekognition_media_analysis_results import RekognitionMediaAnalysisResults


class RekognitionGetMediaAnalysisJobResponse(BaseModel):
    JobId: StrictStr | None = None
    JobName: StrictStr | None = None
    OperationsConfig: RekognitionMediaAnalysisOperationsConfig | None = None
    Status: StrictStr | None = None
    FailureDetails: RekognitionMediaAnalysisJobFailureDetails | None = None
    CreationTimestamp: datetime.datetime | StrictStr | None = None
    CompletionTimestamp: datetime.datetime | StrictStr | None = None
    Input: RekognitionMediaAnalysisInput | None = None
    OutputConfig: RekognitionMediaAnalysisOutputConfig | None = None
    KmsKeyId: StrictStr | None = None
    Results: RekognitionMediaAnalysisResults | None = None
    ManifestSummary: RekognitionMediaAnalysisManifestSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None

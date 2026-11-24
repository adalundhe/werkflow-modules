from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rekognition_media_analysis_input import RekognitionMediaAnalysisInput
from .rekognition_media_analysis_operations_config import RekognitionMediaAnalysisOperationsConfig
from .rekognition_media_analysis_output_config import RekognitionMediaAnalysisOutputConfig


class RekognitionStartMediaAnalysisJobRequest(BaseModel):
    OperationsConfig: RekognitionMediaAnalysisOperationsConfig
    Input: RekognitionMediaAnalysisInput
    OutputConfig: RekognitionMediaAnalysisOutputConfig
    ClientRequestToken: StrictStr | None = None
    JobName: StrictStr | None = None
    KmsKeyId: StrictStr | None = None

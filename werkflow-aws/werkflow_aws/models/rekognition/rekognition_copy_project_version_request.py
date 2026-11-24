from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rekognition_output_config import RekognitionOutputConfig


class RekognitionCopyProjectVersionRequest(BaseModel):
    SourceProjectArn: StrictStr
    SourceProjectVersionArn: StrictStr
    DestinationProjectArn: StrictStr
    VersionName: StrictStr
    OutputConfig: RekognitionOutputConfig
    Tags: dict[StrictStr, StrictStr] | None = None
    KmsKeyId: StrictStr | None = None

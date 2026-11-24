from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rekognition_customization_feature_config import RekognitionCustomizationFeatureConfig
from .rekognition_output_config import RekognitionOutputConfig
from .rekognition_testing_data import RekognitionTestingData
from .rekognition_training_data import RekognitionTrainingData


class RekognitionCreateProjectVersionRequest(BaseModel):
    ProjectArn: StrictStr
    VersionName: StrictStr
    OutputConfig: RekognitionOutputConfig
    TrainingData: RekognitionTrainingData | None = None
    TestingData: RekognitionTestingData | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    KmsKeyId: StrictStr | None = None
    VersionDescription: StrictStr | None = None
    FeatureConfig: RekognitionCustomizationFeatureConfig | None = None

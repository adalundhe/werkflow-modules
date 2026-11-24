from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .rekognition_customization_feature_config import RekognitionCustomizationFeatureConfig
from .rekognition_evaluation_result import RekognitionEvaluationResult
from .rekognition_ground_truth_manifest import RekognitionGroundTruthManifest
from .rekognition_output_config import RekognitionOutputConfig
from .rekognition_testing_data_result import RekognitionTestingDataResult
from .rekognition_training_data_result import RekognitionTrainingDataResult


class RekognitionProjectVersionDescription(BaseModel):
    ProjectVersionArn: StrictStr | None = None
    CreationTimestamp: datetime.datetime | StrictStr | None = None
    MinInferenceUnits: StrictInt | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    BillableTrainingTimeInSeconds: StrictInt | None = None
    TrainingEndTimestamp: datetime.datetime | StrictStr | None = None
    OutputConfig: RekognitionOutputConfig | None = None
    TrainingDataResult: RekognitionTrainingDataResult | None = None
    TestingDataResult: RekognitionTestingDataResult | None = None
    EvaluationResult: RekognitionEvaluationResult | None = None
    ManifestSummary: RekognitionGroundTruthManifest | None = None
    KmsKeyId: StrictStr | None = None
    MaxInferenceUnits: StrictInt | None = None
    SourceProjectVersionArn: StrictStr | None = None
    VersionDescription: StrictStr | None = None
    Feature: StrictStr | None = None
    BaseModelVersion: StrictStr | None = None
    FeatureConfig: RekognitionCustomizationFeatureConfig | None = None

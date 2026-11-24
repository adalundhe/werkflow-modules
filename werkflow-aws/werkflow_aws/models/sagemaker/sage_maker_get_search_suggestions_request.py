from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .sage_maker_suggestion_query import SageMakerSuggestionQuery


class SageMakerGetSearchSuggestionsRequest(BaseModel):
    Resource: Literal['TrainingJob', 'Experiment', 'ExperimentTrial', 'ExperimentTrialComponent', 'Endpoint', 'Model', 'ModelPackage', 'ModelPackageGroup', 'Pipeline', 'PipelineExecution', 'FeatureGroup', 'FeatureMetadata', 'Image', 'ImageVersion', 'Project', 'HyperParameterTuningJob', 'ModelCard', 'PipelineVersion', 'Job', 'HubContent']
    SuggestionQuery: SageMakerSuggestionQuery | None = None

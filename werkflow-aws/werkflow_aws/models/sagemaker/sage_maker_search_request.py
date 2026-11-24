from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_search_expression import SageMakerSearchExpression
from .sage_maker_visibility_conditions import SageMakerVisibilityConditions


class SageMakerSearchRequest(BaseModel):
    Resource: Literal['TrainingJob', 'Experiment', 'ExperimentTrial', 'ExperimentTrialComponent', 'Endpoint', 'Model', 'ModelPackage', 'ModelPackageGroup', 'Pipeline', 'PipelineExecution', 'FeatureGroup', 'FeatureMetadata', 'Image', 'ImageVersion', 'Project', 'HyperParameterTuningJob', 'ModelCard', 'PipelineVersion', 'Job', 'HubContent']
    SearchExpression: SageMakerSearchExpression | None = None
    SortBy: StrictStr | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    CrossAccountFilterOption: Literal['SameAccount', 'CrossAccount'] | None = None
    VisibilityConditions: list[SageMakerVisibilityConditions] | None = None

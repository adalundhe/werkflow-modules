from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_candidate_artifact_locations import SageMakerCandidateArtifactLocations
from .sage_maker_metric_datum import SageMakerMetricDatum


class SageMakerCandidateProperties(BaseModel):
    CandidateArtifactLocations: SageMakerCandidateArtifactLocations | None = None
    CandidateMetrics: list[SageMakerMetricDatum] | None = None

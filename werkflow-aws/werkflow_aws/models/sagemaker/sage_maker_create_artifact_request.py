from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_artifact_source import SageMakerArtifactSource
from .sage_maker_metadata_properties import SageMakerMetadataProperties
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateArtifactRequest(BaseModel):
    Source: SageMakerArtifactSource
    ArtifactType: StrictStr
    ArtifactName: StrictStr | None = None
    Properties: dict[StrictStr, StrictStr] | None = None
    MetadataProperties: SageMakerMetadataProperties | None = None
    Tags: list[SageMakerTagModel] | None = None

from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_artifact_source import SageMakerArtifactSource
from .sage_maker_metadata_properties import SageMakerMetadataProperties
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerDescribeArtifactResponse(BaseModel):
    ArtifactName: StrictStr | None = None
    ArtifactArn: StrictStr | None = None
    Source: SageMakerArtifactSource | None = None
    ArtifactType: StrictStr | None = None
    Properties: dict[StrictStr, StrictStr] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    MetadataProperties: SageMakerMetadataProperties | None = None
    LineageGroupArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None

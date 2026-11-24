from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .comprehend_augmented_manifests_list_item import ComprehendAugmentedManifestsListItem
from .comprehend_entity_recognizer_annotations import ComprehendEntityRecognizerAnnotations
from .comprehend_entity_recognizer_documents import ComprehendEntityRecognizerDocuments
from .comprehend_entity_recognizer_entity_list import ComprehendEntityRecognizerEntityList
from .comprehend_entity_types_list_item import ComprehendEntityTypesListItem


class ComprehendEntityRecognizerInputDataConfig(BaseModel):
    DataFormat: StrictStr | None = None
    EntityTypes: list[ComprehendEntityTypesListItem] | None = None
    Documents: ComprehendEntityRecognizerDocuments | None = None
    Annotations: ComprehendEntityRecognizerAnnotations | None = None
    EntityList: ComprehendEntityRecognizerEntityList | None = None
    AugmentedManifests: list[ComprehendAugmentedManifestsListItem] | None = None

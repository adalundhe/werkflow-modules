from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .comprehend_dataset_augmented_manifests_list_item import ComprehendDatasetAugmentedManifestsListItem
from .comprehend_dataset_document_classifier_input_data_config import ComprehendDatasetDocumentClassifierInputDataConfig
from .comprehend_dataset_entity_recognizer_input_data_config import ComprehendDatasetEntityRecognizerInputDataConfig


class ComprehendDatasetInputDataConfig(BaseModel):
    AugmentedManifests: list[ComprehendDatasetAugmentedManifestsListItem] | None = None
    DataFormat: Literal['COMPREHEND_CSV', 'AUGMENTED_MANIFEST'] | None = None
    DocumentClassifierInputDataConfig: ComprehendDatasetDocumentClassifierInputDataConfig | None = None
    EntityRecognizerInputDataConfig: ComprehendDatasetEntityRecognizerInputDataConfig | None = None

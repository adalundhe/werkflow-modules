from __future__ import annotations
from pydantic import BaseModel
from .awss3_annotation_table_configuration_result import AWSS3AnnotationTableConfigurationResult
from .awss3_destination_result import AWSS3DestinationResult
from .awss3_inventory_table_configuration_result import AWSS3InventoryTableConfigurationResult
from .awss3_journal_table_configuration_result import AWSS3JournalTableConfigurationResult


class AWSS3MetadataConfigurationResult(BaseModel):
    DestinationResult: AWSS3DestinationResult | None = None
    JournalTableConfigurationResult: AWSS3JournalTableConfigurationResult | None = None
    InventoryTableConfigurationResult: AWSS3InventoryTableConfigurationResult | None = None
    AnnotationTableConfigurationResult: AWSS3AnnotationTableConfigurationResult | None = None

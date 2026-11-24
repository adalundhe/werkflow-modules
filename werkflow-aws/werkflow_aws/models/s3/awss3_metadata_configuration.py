from __future__ import annotations
from pydantic import BaseModel
from .awss3_annotation_table_configuration import AWSS3AnnotationTableConfiguration
from .awss3_inventory_table_configuration import AWSS3InventoryTableConfiguration
from .awss3_journal_table_configuration import AWSS3JournalTableConfiguration


class AWSS3MetadataConfiguration(BaseModel):
    JournalTableConfiguration: AWSS3JournalTableConfiguration
    InventoryTableConfiguration: AWSS3InventoryTableConfiguration | None = None
    AnnotationTableConfiguration: AWSS3AnnotationTableConfiguration | None = None

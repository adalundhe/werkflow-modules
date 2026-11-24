from __future__ import annotations
from pydantic import BaseModel
from .health_imaging_dicom_metadata_mapping import HealthImagingDicomMetadataMapping


class HealthImagingDicomJsonMetadataImportConfiguration(BaseModel):
    dicomMetadataMappings: list[HealthImagingDicomMetadataMapping] | None = None

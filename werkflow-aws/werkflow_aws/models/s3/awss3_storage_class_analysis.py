from __future__ import annotations
from pydantic import BaseModel
from .awss3_storage_class_analysis_data_export import AWSS3StorageClassAnalysisDataExport


class AWSS3StorageClassAnalysis(BaseModel):
    DataExport: AWSS3StorageClassAnalysisDataExport | None = None

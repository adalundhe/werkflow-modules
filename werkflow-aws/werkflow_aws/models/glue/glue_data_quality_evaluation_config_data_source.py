from __future__ import annotations
from pydantic import BaseModel
from .glue_data_quality_evaluation_config_glue_tables import GlueDataQualityEvaluationConfigGlueTables


class GlueDataQualityEvaluationConfigDataSource(BaseModel):
    GlueTables: GlueDataQualityEvaluationConfigGlueTables | None = None

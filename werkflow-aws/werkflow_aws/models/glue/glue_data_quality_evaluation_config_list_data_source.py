from __future__ import annotations
from pydantic import BaseModel
from .glue_data_quality_evaluation_config_list_glue_tables import GlueDataQualityEvaluationConfigListGlueTables


class GlueDataQualityEvaluationConfigListDataSource(BaseModel):
    GlueTables: GlueDataQualityEvaluationConfigListGlueTables | None = None

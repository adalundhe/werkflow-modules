from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_export_labels_task_run_properties import GlueExportLabelsTaskRunProperties
from .glue_find_matches_task_run_properties import GlueFindMatchesTaskRunProperties
from .glue_import_labels_task_run_properties import GlueImportLabelsTaskRunProperties
from .glue_labeling_set_generation_task_run_properties import GlueLabelingSetGenerationTaskRunProperties


class GlueTaskRunProperties(BaseModel):
    TaskType: StrictStr | None = None
    ImportLabelsTaskRunProperties: GlueImportLabelsTaskRunProperties | None = None
    ExportLabelsTaskRunProperties: GlueExportLabelsTaskRunProperties | None = None
    LabelingSetGenerationTaskRunProperties: GlueLabelingSetGenerationTaskRunProperties | None = None
    FindMatchesTaskRunProperties: GlueFindMatchesTaskRunProperties | None = None

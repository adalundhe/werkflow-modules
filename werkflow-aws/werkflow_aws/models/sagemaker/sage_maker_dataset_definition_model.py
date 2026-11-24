from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_athena_dataset_definition_model import SageMakerAthenaDatasetDefinitionModel
from .sage_maker_redshift_dataset_definition_model import SageMakerRedshiftDatasetDefinitionModel


class SageMakerDatasetDefinitionModel(BaseModel):
    AthenaDatasetDefinition: SageMakerAthenaDatasetDefinitionModel | None = None
    RedshiftDatasetDefinition: SageMakerRedshiftDatasetDefinitionModel | None = None
    LocalPath: StrictStr | None = None
    DataDistributionType: StrictStr | None = None
    InputMode: StrictStr | None = None

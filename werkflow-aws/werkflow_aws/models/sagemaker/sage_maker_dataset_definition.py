from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_athena_dataset_definition import SageMakerAthenaDatasetDefinition
from .sage_maker_data_distribution_type import SageMakerDataDistributionType
from .sage_maker_input_mode import SageMakerInputMode
from .sage_maker_redshift_dataset_definition import SageMakerRedshiftDatasetDefinition


class SageMakerDatasetDefinition(BaseModel):
    AthenaDatasetDefinition: SageMakerAthenaDatasetDefinition | None = None
    RedshiftDatasetDefinition: SageMakerRedshiftDatasetDefinition | None = None
    LocalPath: StrictStr | None = None
    DataDistributionType: SageMakerDataDistributionType | None = None
    InputMode: SageMakerInputMode | None = None

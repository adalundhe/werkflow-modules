from pydantic import BaseModel, StrictStr, model_validator
from typing import Literal, Self

GroupTypes = Literal[
    "DIMENSION",
    "TAG",
    "COST_CATEGORY"
]

DimensionTypes = Literal[
    "AZ",
    "INSTANCE_TYPE",
    "LEGAL_ENTITY_NAME",
    "INVOICING_ENTITY",
    "LINKED_ACCOUNT",
    "OPERATION",
    "PLATFORM",
    "PURCHASE_TYPE",
    "SERVICE",
    "TENANCY",
    "RECORD_TYPE",
    "USAGE_TYPE",
]

class Group(BaseModel):
    Type: GroupTypes
    Key: DimensionTypes | StrictStr

    @model_validator(mode='after')
    def validate_dimension_types(self) -> Self:
        dimension_types = [
            "AZ",
            "INSTANCE_TYPE",
            "LEGAL_ENTITY_NAME",
            "INVOICING_ENTITY",
            "LINKED_ACCOUNT",
            "OPERATION",
            "PLATFORM",
            "PURCHASE_TYPE",
            "SERVICE",
            "TENANCY",
            "RECORD_TYPE",
            "USAGE_TYPE",
        ]

        if self.Type == 'DIMENSION' and self.Key not in dimension_types:
            valid_types = ', '.join(dimension_types)
            raise ValueError(f'Invalid Dimension type {self.Key} - must be one of {valid_types}')
        
        return self
    
    def dump(self):
        return self.model_dump()
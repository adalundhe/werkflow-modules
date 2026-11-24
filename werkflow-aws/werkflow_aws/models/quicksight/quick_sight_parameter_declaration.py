from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_date_time_parameter_declaration import QuickSightDateTimeParameterDeclaration
from .quick_sight_decimal_parameter_declaration import QuickSightDecimalParameterDeclaration
from .quick_sight_integer_parameter_declaration import QuickSightIntegerParameterDeclaration
from .quick_sight_string_parameter_declaration import QuickSightStringParameterDeclaration


class QuickSightParameterDeclaration(BaseModel):
    StringParameterDeclaration: QuickSightStringParameterDeclaration | None = None
    DecimalParameterDeclaration: QuickSightDecimalParameterDeclaration | None = None
    IntegerParameterDeclaration: QuickSightIntegerParameterDeclaration | None = None
    DateTimeParameterDeclaration: QuickSightDateTimeParameterDeclaration | None = None

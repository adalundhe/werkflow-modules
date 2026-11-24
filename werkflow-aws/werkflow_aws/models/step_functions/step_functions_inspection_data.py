from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .step_functions_inspection_data_request import StepFunctionsInspectionDataRequest
from .step_functions_inspection_data_response import StepFunctionsInspectionDataResponse
from .step_functions_inspection_error_details import StepFunctionsInspectionErrorDetails


class StepFunctionsInspectionData(BaseModel):
    input: StrictStr | None = None
    afterArguments: StrictStr | None = None
    afterInputPath: StrictStr | None = None
    afterParameters: StrictStr | None = None
    result: StrictStr | None = None
    afterResultSelector: StrictStr | None = None
    afterResultPath: StrictStr | None = None
    request: StepFunctionsInspectionDataRequest | None = None
    response: StepFunctionsInspectionDataResponse | None = None
    variables: StrictStr | None = None
    errorDetails: StepFunctionsInspectionErrorDetails | None = None
    afterItemsPath: StrictStr | None = None
    afterItemSelector: StrictStr | None = None
    afterItemBatcher: StrictStr | None = None
    afterItemsPointer: StrictStr | None = None
    toleratedFailureCount: StrictInt | None = None
    toleratedFailurePercentage: StrictFloat | StrictInt | None = None
    maxConcurrency: StrictInt | None = None

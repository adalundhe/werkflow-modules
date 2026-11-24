from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class JsonNode(BaseModel):
    array: StrictBool | None = None
    bigDecimal: StrictBool | None = None
    bigInteger: StrictBool | None = None
    bigIntegerValue: StrictInt | None = None
    binary: StrictBool | None = None
    binaryValue: list[StrictStr] | None = None
    boolean: StrictBool | None = None
    booleanValue: StrictBool | None = None
    containerNode: StrictBool | None = None
    decimalValue: StrictFloat | StrictInt | None = None
    double: StrictBool | None = None
    doubleValue: StrictFloat | StrictInt | None = None
    elements: dict[StrictStr, Any] | None = None
    fieldNames: dict[StrictStr, Any] | None = None
    fields: dict[StrictStr, Any] | None = None
    floatingPointNumber: StrictBool | None = None
    int: StrictBool | None = None
    intValue: StrictInt | None = None
    integralNumber: StrictBool | None = None
    long: StrictBool | None = None
    longValue: StrictInt | None = None
    missingNode: StrictBool | None = None
    null: StrictBool | None = None
    number: StrictBool | None = None
    numberType: StrictStr | None = None
    numberValue: StrictFloat | StrictInt | None = None
    object: StrictBool | None = None
    pojo: StrictBool | None = None
    textValue: StrictStr | None = None
    textual: StrictBool | None = None
    valueAsBoolean: StrictBool | None = None
    valueAsDouble: StrictFloat | StrictInt | None = None
    valueAsInt: StrictInt | None = None
    valueAsLong: StrictInt | None = None
    valueAsText: StrictStr | None = None
    valueNode: StrictBool | None = None

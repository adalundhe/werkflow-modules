from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_dialog_code_hook_settings import LexDialogCodeHookSettings
from .lex_fulfillment_code_hook_settings import LexFulfillmentCodeHookSettings
from .lex_initial_response_setting import LexInitialResponseSetting
from .lex_input_context import LexInputContext
from .lex_intent_closing_setting import LexIntentClosingSetting
from .lex_intent_confirmation_setting import LexIntentConfirmationSetting
from .lex_kendra_configuration import LexKendraConfiguration
from .lex_output_context import LexOutputContext
from .lex_q_in_connect_intent_configuration import LexQInConnectIntentConfiguration
from .lex_qn_a_intent_configuration import LexQnAIntentConfiguration
from .lex_sample_utterance import LexSampleUtterance
from .lex_slot_priority import LexSlotPriority


class LexDescribeIntentResponse(BaseModel):
    intentId: StrictStr | None = None
    intentName: StrictStr | None = None
    intentDisplayName: StrictStr | None = None
    description: StrictStr | None = None
    parentIntentSignature: StrictStr | None = None
    sampleUtterances: list[LexSampleUtterance] | None = None
    dialogCodeHook: LexDialogCodeHookSettings | None = None
    fulfillmentCodeHook: LexFulfillmentCodeHookSettings | None = None
    slotPriorities: list[LexSlotPriority] | None = None
    intentConfirmationSetting: LexIntentConfirmationSetting | None = None
    intentClosingSetting: LexIntentClosingSetting | None = None
    inputContexts: list[LexInputContext] | None = None
    outputContexts: list[LexOutputContext] | None = None
    kendraConfiguration: LexKendraConfiguration | None = None
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    initialResponseSetting: LexInitialResponseSetting | None = None
    qnAIntentConfiguration: LexQnAIntentConfiguration | None = None
    qInConnectIntentConfiguration: LexQInConnectIntentConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None

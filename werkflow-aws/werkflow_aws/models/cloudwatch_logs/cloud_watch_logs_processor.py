from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_logs_add_keys import CloudWatchLogsAddKeys
from .cloud_watch_logs_csv import CloudWatchLogsCSV
from .cloud_watch_logs_copy_value import CloudWatchLogsCopyValue
from .cloud_watch_logs_date_time_converter import CloudWatchLogsDateTimeConverter
from .cloud_watch_logs_delete_keys import CloudWatchLogsDeleteKeys
from .cloud_watch_logs_grok import CloudWatchLogsGrok
from .cloud_watch_logs_list_to_map import CloudWatchLogsListToMap
from .cloud_watch_logs_lower_case_string import CloudWatchLogsLowerCaseString
from .cloud_watch_logs_move_keys import CloudWatchLogsMoveKeys
from .cloud_watch_logs_parse_cloudfront import CloudWatchLogsParseCloudfront
from .cloud_watch_logs_parse_json import CloudWatchLogsParseJSON
from .cloud_watch_logs_parse_key_value import CloudWatchLogsParseKeyValue
from .cloud_watch_logs_parse_postgres import CloudWatchLogsParsePostgres
from .cloud_watch_logs_parse_route53 import CloudWatchLogsParseRoute53
from .cloud_watch_logs_parse_to_ocsf import CloudWatchLogsParseToOCSF
from .cloud_watch_logs_parse_vpc import CloudWatchLogsParseVPC
from .cloud_watch_logs_parse_waf import CloudWatchLogsParseWAF
from .cloud_watch_logs_rename_keys import CloudWatchLogsRenameKeys
from .cloud_watch_logs_split_string import CloudWatchLogsSplitString
from .cloud_watch_logs_substitute_string import CloudWatchLogsSubstituteString
from .cloud_watch_logs_trim_string import CloudWatchLogsTrimString
from .cloud_watch_logs_type_converter import CloudWatchLogsTypeConverter
from .cloud_watch_logs_upper_case_string import CloudWatchLogsUpperCaseString


class CloudWatchLogsProcessor(BaseModel):
    addKeys: CloudWatchLogsAddKeys | None = None
    copyValue: CloudWatchLogsCopyValue | None = None
    csv: CloudWatchLogsCSV | None = None
    dateTimeConverter: CloudWatchLogsDateTimeConverter | None = None
    deleteKeys: CloudWatchLogsDeleteKeys | None = None
    grok: CloudWatchLogsGrok | None = None
    listToMap: CloudWatchLogsListToMap | None = None
    lowerCaseString: CloudWatchLogsLowerCaseString | None = None
    moveKeys: CloudWatchLogsMoveKeys | None = None
    parseCloudfront: CloudWatchLogsParseCloudfront | None = None
    parseJSON: CloudWatchLogsParseJSON | None = None
    parseKeyValue: CloudWatchLogsParseKeyValue | None = None
    parseRoute53: CloudWatchLogsParseRoute53 | None = None
    parseToOCSF: CloudWatchLogsParseToOCSF | None = None
    parsePostgres: CloudWatchLogsParsePostgres | None = None
    parseVPC: CloudWatchLogsParseVPC | None = None
    parseWAF: CloudWatchLogsParseWAF | None = None
    renameKeys: CloudWatchLogsRenameKeys | None = None
    splitString: CloudWatchLogsSplitString | None = None
    substituteString: CloudWatchLogsSubstituteString | None = None
    trimString: CloudWatchLogsTrimString | None = None
    typeConverter: CloudWatchLogsTypeConverter | None = None
    upperCaseString: CloudWatchLogsUpperCaseString | None = None

from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_process_details import GuardDutyProcessDetails


class GuardDutyRuntimeContext(BaseModel):
    ModifyingProcess: GuardDutyProcessDetails | None = None
    ModifiedAt: datetime.datetime | StrictStr | None = None
    ScriptPath: StrictStr | None = None
    LibraryPath: StrictStr | None = None
    LdPreloadValue: StrictStr | None = None
    SocketPath: StrictStr | None = None
    RuncBinaryPath: StrictStr | None = None
    ReleaseAgentPath: StrictStr | None = None
    MountSource: StrictStr | None = None
    MountTarget: StrictStr | None = None
    FileSystemType: StrictStr | None = None
    Flags: list[StrictStr] | None = None
    ModuleName: StrictStr | None = None
    ModuleFilePath: StrictStr | None = None
    ModuleSha256: StrictStr | None = None
    ShellHistoryFilePath: StrictStr | None = None
    TargetProcess: GuardDutyProcessDetails | None = None
    AddressFamily: StrictStr | None = None
    IanaProtocolNumber: StrictInt | None = None
    MemoryRegions: list[StrictStr] | None = None
    ToolName: StrictStr | None = None
    ToolCategory: StrictStr | None = None
    ServiceName: StrictStr | None = None
    CommandLineExample: StrictStr | None = None
    ThreatFilePath: StrictStr | None = None
    FileOperation: StrictStr | None = None
    FilePath: StrictStr | None = None
    RelatedFilePaths: list[StrictStr] | None = None

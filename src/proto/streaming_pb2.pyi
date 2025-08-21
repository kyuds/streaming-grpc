from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResponseStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OK: _ClassVar[ResponseStatus]
    ERROR: _ClassVar[ResponseStatus]
    DONE: _ClassVar[ResponseStatus]
OK: ResponseStatus
ERROR: ResponseStatus
DONE: ResponseStatus

class StreamRequest(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class StreamResponse(_message.Message):
    __slots__ = ("message", "sequence_number", "timestamp", "status")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    sequence_number: int
    timestamp: int
    status: ResponseStatus
    def __init__(self, message: _Optional[str] = ..., sequence_number: _Optional[int] = ..., timestamp: _Optional[int] = ..., status: _Optional[_Union[ResponseStatus, str]] = ...) -> None: ...

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: customer_record.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='customer_record.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x15\x63ustomer_record.proto\"8\n\x0e\x43ustomerRecord\x12\x15\n\rcustomer_name\x18\x01 \x01(\t\x12\x0f\n\x07row_num\x18\x02 \x02(\x03')
)




_CUSTOMERRECORD = _descriptor.Descriptor(
  name='CustomerRecord',
  full_name='CustomerRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_name', full_name='CustomerRecord.customer_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='row_num', full_name='CustomerRecord.row_num', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=81,
)

DESCRIPTOR.message_types_by_name['CustomerRecord'] = _CUSTOMERRECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomerRecord = _reflection.GeneratedProtocolMessageType('CustomerRecord', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMERRECORD,
  __module__ = 'customer_record_pb2'
  # @@protoc_insertion_point(class_scope:CustomerRecord)
  ))
_sym_db.RegisterMessage(CustomerRecord)


# @@protoc_insertion_point(module_scope)

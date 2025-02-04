# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: computer-orders.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='computer-orders.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x63omputer-orders.proto\"\x94\x02\n\x0cOrderMessage\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12$\n\x06status\x18\x03 \x01(\x0e\x32\x14.OrderMessage.Status\x12\x12\n\ncreated_at\x18\x04 \x01(\t\x12*\n\tequipment\x18\x05 \x03(\x0e\x32\x17.OrderMessage.Equipment\"?\n\x06Status\x12\n\n\x06QUEUED\x10\x00\x12\x0e\n\nPROCESSING\x10\x01\x12\r\n\tCOMPLETED\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\"=\n\tEquipment\x12\x0c\n\x08KEYBOARD\x10\x00\x12\t\n\x05MOUSE\x10\x01\x12\n\n\x06WEBCAM\x10\x02\x12\x0b\n\x07MONITOR\x10\x03\"\x07\n\x05\x45mpty\"1\n\x10OrderMessageList\x12\x1d\n\x06orders\x18\x01 \x03(\x0b\x32\r.OrderMessage2X\n\x0cOrderService\x12&\n\x06\x43reate\x12\r.OrderMessage\x1a\r.OrderMessage\x12 \n\x03Get\x12\x06.Empty\x1a\x11.OrderMessageListb\x06proto3'
)



_ORDERMESSAGE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='OrderMessage.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='QUEUED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROCESSING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=176,
  serialized_end=239,
)
_sym_db.RegisterEnumDescriptor(_ORDERMESSAGE_STATUS)

_ORDERMESSAGE_EQUIPMENT = _descriptor.EnumDescriptor(
  name='Equipment',
  full_name='OrderMessage.Equipment',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KEYBOARD', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MOUSE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WEBCAM', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MONITOR', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=241,
  serialized_end=302,
)
_sym_db.RegisterEnumDescriptor(_ORDERMESSAGE_EQUIPMENT)


_ORDERMESSAGE = _descriptor.Descriptor(
  name='OrderMessage',
  full_name='OrderMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='OrderMessage.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_by', full_name='OrderMessage.created_by', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='OrderMessage.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='OrderMessage.created_at', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='equipment', full_name='OrderMessage.equipment', index=4,
      number=5, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ORDERMESSAGE_STATUS,
    _ORDERMESSAGE_EQUIPMENT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=302,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=304,
  serialized_end=311,
)


_ORDERMESSAGELIST = _descriptor.Descriptor(
  name='OrderMessageList',
  full_name='OrderMessageList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='orders', full_name='OrderMessageList.orders', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=313,
  serialized_end=362,
)

_ORDERMESSAGE.fields_by_name['status'].enum_type = _ORDERMESSAGE_STATUS
_ORDERMESSAGE.fields_by_name['equipment'].enum_type = _ORDERMESSAGE_EQUIPMENT
_ORDERMESSAGE_STATUS.containing_type = _ORDERMESSAGE
_ORDERMESSAGE_EQUIPMENT.containing_type = _ORDERMESSAGE
_ORDERMESSAGELIST.fields_by_name['orders'].message_type = _ORDERMESSAGE
DESCRIPTOR.message_types_by_name['OrderMessage'] = _ORDERMESSAGE
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['OrderMessageList'] = _ORDERMESSAGELIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrderMessage = _reflection.GeneratedProtocolMessageType('OrderMessage', (_message.Message,), {
  'DESCRIPTOR' : _ORDERMESSAGE,
  '__module__' : 'computer_orders_pb2'
  # @@protoc_insertion_point(class_scope:OrderMessage)
  })
_sym_db.RegisterMessage(OrderMessage)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'computer_orders_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

OrderMessageList = _reflection.GeneratedProtocolMessageType('OrderMessageList', (_message.Message,), {
  'DESCRIPTOR' : _ORDERMESSAGELIST,
  '__module__' : 'computer_orders_pb2'
  # @@protoc_insertion_point(class_scope:OrderMessageList)
  })
_sym_db.RegisterMessage(OrderMessageList)



_ORDERSERVICE = _descriptor.ServiceDescriptor(
  name='OrderService',
  full_name='OrderService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=364,
  serialized_end=452,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='OrderService.Create',
    index=0,
    containing_service=None,
    input_type=_ORDERMESSAGE,
    output_type=_ORDERMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='OrderService.Get',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_ORDERMESSAGELIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORDERSERVICE)

DESCRIPTOR.services_by_name['OrderService'] = _ORDERSERVICE

# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: my_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10my_service.proto\x12\tmyservice\" \n\x04Item\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x14\n\x06ItemId\x12\n\n\x02id\x18\x01 \x01(\t2\xd6\x01\n\x0bItemService\x12\x30\n\nCreateItem\x12\x0f.myservice.Item\x1a\x0f.myservice.Item\"\x00\x12/\n\x07GetItem\x12\x11.myservice.ItemId\x1a\x0f.myservice.Item\"\x00\x12\x30\n\nUpdateItem\x12\x0f.myservice.Item\x1a\x0f.myservice.Item\"\x00\x12\x32\n\nDeleteItem\x12\x11.myservice.ItemId\x1a\x0f.myservice.Item\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'my_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ITEM']._serialized_start=31
  _globals['_ITEM']._serialized_end=63
  _globals['_ITEMID']._serialized_start=65
  _globals['_ITEMID']._serialized_end=85
  _globals['_ITEMSERVICE']._serialized_start=88
  _globals['_ITEMSERVICE']._serialized_end=302
# @@protoc_insertion_point(module_scope)
#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class Unknown:
  """
  Attributes:
   - temp
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'temp', None, None, ), # 1
  )

  def __init__(self, temp=None,):
    self.temp = temp

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.temp = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Unknown')
    if self.temp is not None:
      oprot.writeFieldBegin('temp', TType.I32, 1)
      oprot.writeI32(self.temp)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class loginWithIdentityCredentialForCertificateResult:
  """
  Attributes:
   - keepLoggedIn
   - systemName
   - certificate
  """

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'keepLoggedIn', None, None, ), # 1
    (2, TType.I32, 'systemName', None, None, ), # 2
    (3, TType.STRING, 'certificate', None, None, ), # 3
  )

  def __init__(self, keepLoggedIn=None, systemName=None, certificate=None,):
    self.keepLoggedIn = keepLoggedIn
    self.systemName = systemName
    self.certificate = certificate

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.BOOL:
          self.keepLoggedIn = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.systemName = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.certificate = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('loginWithIdentityCredentialForCertificateResult')
    if self.keepLoggedIn is not None:
      oprot.writeFieldBegin('keepLoggedIn', TType.BOOL, 1)
      oprot.writeBool(self.keepLoggedIn)
      oprot.writeFieldEnd()
    if self.systemName is not None:
      oprot.writeFieldBegin('systemName', TType.I32, 2)
      oprot.writeI32(self.systemName)
      oprot.writeFieldEnd()
    if self.certificate is not None:
      oprot.writeFieldBegin('certificate', TType.STRING, 3)
      oprot.writeString(self.certificate)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class loginWithIdentityCredentialForCertificateResult2:
  """
  Attributes:
   - keepLoggedIn
   - systemName
   - certificate
  """

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'keepLoggedIn', None, None, ), # 1
    (2, TType.I32, 'systemName', None, None, ), # 2
    (3, TType.STRING, 'certificate', None, None, ), # 3
  )

  def __init__(self, keepLoggedIn=None, systemName=None, certificate=None,):
    self.keepLoggedIn = keepLoggedIn
    self.systemName = systemName
    self.certificate = certificate

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.BOOL:
          self.keepLoggedIn = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.systemName = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.certificate = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('loginWithIdentityCredentialForCertificateResult2')
    if self.keepLoggedIn is not None:
      oprot.writeFieldBegin('keepLoggedIn', TType.BOOL, 1)
      oprot.writeBool(self.keepLoggedIn)
      oprot.writeFieldEnd()
    if self.systemName is not None:
      oprot.writeFieldBegin('systemName', TType.I32, 2)
      oprot.writeI32(self.systemName)
      oprot.writeFieldEnd()
    if self.certificate is not None:
      oprot.writeFieldBegin('certificate', TType.STRING, 3)
      oprot.writeString(self.certificate)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

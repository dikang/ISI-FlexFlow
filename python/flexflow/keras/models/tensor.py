import flexflow.core as ff

class Tensor(object):
  __slots__ = ['_ffhandle', 'to_layers', 'from_layer', 'dtype', \
               'batch_shape', 'name', 'num_dims']
  def __init__(self, ffmodel=None, 
               shape=None, batch_size=None,
               name=None, dtype=None, 
               sparse=False, tensor=None, ragged=False,
               meta_only=False, ffhandle=None, **kwargs):
    if sparse != False:
      assert 0, "sparse is not supported"
    if tensor != None:
      assert 0, "tensor is not supported"
    if ragged != False:
      assert 0, "ragged is not supported"
      
    batch_shape = None
    if "batch_shape" in kwargs:
      batch_shape = kwargs["batch_shape"]
               
    self._ffhandle = ffhandle
    self.to_layers = []
    self.from_layer = 0
    if dtype == None or dtype == "float32" or dtype == ff.DataType.DT_FLOAT:
      self.dtype = ff.DataType.DT_FLOAT
    elif dtype == "float64" or dtype == ff.DataType.DT_DOUBLE:
      self.dtype = ff.DataType.DT_DOUBLE
    elif dtype == "int32" or dtype == ff.DataType.DT_INT32:
      self.dtype = ff.DataType.DT_INT32
    elif dtype == "int64" or dtype == ff.DataType.DT_INT64:
      self.dtype = ff.DataType.DT_INT64
    else:
      assert 0, "not supported"
    
    if name == None:
      self.name = ""
    else:
      self.name = name
    
    # create a tensor
    if ffhandle == None:
      if batch_shape != None:
        self.batch_shape = batch_shape
        self.num_dims = len(batch_shape)
      else:
        self.num_dims = len(shape) + 1
        if batch_size == None:
          self.batch_shape = (0,) + shape
        else:
          self.batch_shape = (batch_size,) + shape
      if (meta_only == False):
        self.create_ff_tensor(ffmodel)
    # init from handle
    else:
      self.batch_shape = ffhandle.dims
      self.num_dims = ffhandle.num_dims
  
  @property
  def ffhandle(self):
    return self._ffhandle
  
  @ffhandle.setter    
  def ffhandle(self, handle):
    assert isinstance(handle, ff.Tensor) == True, "[Tensor]: ffhandle is not the correct type"
    assert self._ffhandle == None, "[Tensor]: check handle, already set"
    self._ffhandle = handle
    if (self.batch_shape[0] == 0):
      self.set_batch_size(handle.dims[0])
    self.__verify_ffhandle_shape()
    
  def create_ff_tensor(self, ffmodel):
    if (self.num_dims == 2 or self.num_dims == 4):
      self._ffhandle = ffmodel.create_tensor(self.batch_shape, self.name, self.dtype);
    else:
      assert 0, "un-supported dims"
    self.__verify_ffhandle_shape()
    
  def set_from_layer(self, layer):
    assert self.from_layer == 0, "[Tensor]: from layer has been set"
    self.from_layer = layer
    
  def set_to_layer(self, layer):
    self.to_layers.append(layer)
    
  def set_batch_size(self, size):
    lst = list(self.batch_shape)
    lst[0] = size
    self.batch_shape = tuple(lst)
    
  def __verify_ffhandle_shape(self):
    assert self.num_dims == self._ffhandle.num_dims, "[Tensor]: check tensor shape"
    for i in range(0, self.num_dims):
      assert self.batch_shape[i] == self._ffhandle.dims[i], "[Tensor]: please check shape dim %d (%d == %d)" %(i, self.batch_shape[i], self._ffhandle.dims[i])
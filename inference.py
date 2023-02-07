import onnxruntime
import torch
import numpy as np
from onnxruntime_extensions import get_library_path as _lib_path
from onnxruntime_extensions import PyOrtFunction

from onnxruntime_extensions import onnx_op, PyOp

@onnx_op(op_type="hmm_sleep::today_is_aggregation", inputs=[PyOp.dt_float, PyOp.dt_float])
def today_is_aggregation(adj, x):
    adj = torch.Tensor(adj)
    x = torch.Tensor(x)
    return torch.dot(adj, x)

so = onnxruntime.SessionOptions()
so.register_custom_ops_library(_lib_path())

sess = onnxruntime.InferenceSession("model.onnx", so)

x = np.ones([2]).astype(np.float32)
y = np.ones([2]).astype(np.float32)

print(sess.run(['result'], {'Adjacency matrix': x, 'X': y}))
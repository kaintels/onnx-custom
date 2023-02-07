import torch
from torch.onnx import register_custom_op_symbolic

torch.ops.load_library("build/lib.linux-x86_64-3.8/today_is_aggregation.cpython-38-x86_64-linux-gnu.so")

def today_is_aggregation(g, adj, X):
    return g.op("hmm_sleep::today_is_aggregation", adj, X)

class CustomModel(torch.nn.Module):
    def forward(self, adj, x):
        return torch.ops.hmm_sleep.today_is_aggregation(adj, x)

adj = torch.ones((2))
X = torch.ones((2))

print(adj.shape)

model = CustomModel()
register_custom_op_symbolic("hmm_sleep::today_is_aggregation", today_is_aggregation, 9)

torch.onnx.export(CustomModel(), (adj, X), "model.onnx", opset_version=9, input_names=["Adjacency matrix", "X"], output_names=["result"])
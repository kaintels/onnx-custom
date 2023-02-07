#include <torch/torch.h>

torch::Tensor today_is_aggregation(torch::Tensor Adj, torch::Tensor X){
    torch::Tensor output = torch::dot(Adj, X);
    return output.clone();
}

static auto registry = torch::RegisterOperators("hmm_sleep::today_is_aggregation", &today_is_aggregation);
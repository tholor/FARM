import torch
from torch.utils.data import TensorDataset


# TODO we need the option to handle different dtypes
def convert_features_to_dataset(features):
    """
    Converts a list of feature dictionaries (one for each sample) into a PyTorch Dataset.

    :param features: A list of dictionaries. Each dictionary corresponds to one sample. Its keys are the
                     names of the type of feature and the keys are the features themselves.
    :Return: a Pytorch dataset and a list of tensor names.
    """
    tensor_names = features[0].keys()
    all_tensors = []
    for t_name in tensor_names:
        cur_tensor = torch.tensor(
            [sample[t_name] for sample in features], dtype=torch.long
        )
        all_tensors.append(cur_tensor)

    dataset = TensorDataset(*all_tensors)
    return dataset, tensor_names

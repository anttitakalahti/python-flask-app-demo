import json
import numpy
import os
import torch
import torchvision
import torch.nn.functional as F
import torch.optim as optim
from net import Net

"""
    adapted from:  https://nextjournal.com/gkoehler/pytorch-mnist
"""

batch_size_train = 64
dirname = os.path.dirname(__file__)
TRAINING_EPOCHS = 3
log_interval = 10
MODEL_PATH = os.path.join(dirname, 'results/model.pth')
OPTIMIZER_PATH = os.path.join(dirname, 'results/optimizer.pth')
network = Net()
optimizer = optim.SGD(
    network.parameters(),
    lr=0.01,
    momentum=0.5)

train_loader = torch.utils.data.DataLoader(
  torchvision.datasets.MNIST(
      os.path.join(dirname, 'files/'),
      train=True,
      download=True,
      transform=torchvision.transforms.Compose([
          torchvision.transforms.ToTensor(),
          torchvision.transforms.Normalize(
              (0.1307,), (0.3081,))
      ])
  ),
  batch_size=batch_size_train, shuffle=True)


def initialize_model():
    if os.path.exists(MODEL_PATH):
        load_model()
    else:
        for epoch in range(1, TRAINING_EPOCHS + 1):
            train(epoch)


def load_model():
    network.load_state_dict(torch.load(MODEL_PATH))
    optimizer.load_state_dict(torch.load(OPTIMIZER_PATH))
    network.eval()


def train(epoch):
    network.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        print(data.shape)
        optimizer.zero_grad()
        output = network(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))
            torch.save(network.state_dict(), MODEL_PATH)
            torch.save(optimizer.state_dict(), OPTIMIZER_PATH)


def predict(image: numpy.ndarray) -> str:
    output = network(image)
    prediction = output.data.max(1, keepdim=True)[1].item()

    return json.dumps({"predicted_label": prediction})




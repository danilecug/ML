#Author: Zhi Zhong

import sys 
import torch 
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

torch.manual_seed(1)

## LSTM cell (input->3, output->3)
lstm = nn.LSTM(3,3)
inputs = [autograd.Variable(torch.randn((1,3))) for _ in range(5)]
print(inputs)


hidden = (autograd.Variable(torch.randn((1,1,3)),
	autograd.Variable(torch.randn((1,1,3))))

print(hidden) 


for i in inputs:
    out, hidden = lstm(i.view(1,1,-1), hidden)
    print(out)
    print(hidden)



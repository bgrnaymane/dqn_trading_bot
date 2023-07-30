from collections import deque, namedtuple
import random
from typing import Deque
from DRLTRGlobalParams import *

import numpy as np
from collections import namedtuple

Transition = namedtuple("Transition", ["States", "Actions", "Rewards", "NextStates", "Dones"])


class ReplayMemory:
  """
  Implementation of Agent memory
  """
  def __init__(self, capacity=MEMORY_LEN):
    self.memory = Deque(maxlen=capacity)

  def store(self, t):
    self.memory.append(t)

  def sample(self, n):
    a = random.sample(self.memory, n)
    return a

  def __len__(self):
    return len(self.memory)
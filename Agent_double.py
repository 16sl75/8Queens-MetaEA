import torch
import torch.nn as nn
import random
from DQN_torch import DQN, DuelingDQN, NDQN
import numpy as np
from collections import deque

class DQNAgent:

    def __init__(self, state_space, action_space, gamma, lr, epsilon, buffer
                 ):

        # Define DQN Layers
        
        self.state_space = state_space
        self.action_space = action_space
        self.gamma = gamma
        self.update_rate = 10
        self.epsilon=epsilon
        self.buffer=buffer
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.l1 = nn.SmoothL1Loss().to(self.device) # Also known as Huber loss
        self.l2 = nn.MSELoss().to(self.device)
        self.lr = lr
        self.replay_buffer = deque(maxlen=self.buffer)

        self.main_network = NDQN(state_space, action_space).to(self.device)
        self.target_network = NDQN(state_space, action_space).to(self.device)

        main_state_dict=self.main_network.state_dict()
        self.target_network.load_state_dict(main_state_dict)


    def store_transistion(self, state, action, reward, next_state, done):
        self.replay_buffer.append((state, action, reward, next_state, done))
        

    # epsilon-greedy policy
    def epsilon_greedy(self, state):

        if random.uniform(0,1) < self.epsilon:
            return np.random.randint(self.action_space)
        
        state = torch.from_numpy(state).to(self.device).float()
        
        Q_values = self.main_network(state)

        self.epsilon -= (self.epsilon - 0.01)/10000
        
        return torch.argmax(Q_values[0])

    
    #train the network
    def train(self, batch_size):
        
        minibatch = random.sample(self.replay_buffer, batch_size)

        state, action, reward, next_state, done = zip(*minibatch)
        
        self.optimizer = torch.optim.Adam(self.main_network.parameters(), lr=self.lr)

        

        state = torch.FloatTensor(np.array(state)).squeeze(1).to(self.device)
        next_state = torch.FloatTensor(np.array(next_state)).squeeze(1).to(self.device)
        action = torch.LongTensor(action).view(batch_size, -1).to(self.device)
        reward = torch.FloatTensor(reward).to(self.device)
        done = torch.FloatTensor(done).to(self.device)
        
        
     
        
        #compute the current Q value using the main network
        target_Q = reward + (1-done)*self.gamma * torch.amax(self.target_network(next_state), dim=1).view(-1, batch_size)
        current_Q = self.main_network(state).gather(1, action).view(-1, batch_size)
        
        loss = self.l2(current_Q, target_Q)
        
        self.optimizer.zero_grad()

        loss.backward()
        
        self.optimizer.step() 

        return loss

    #update the target network weights by copying from the main network
    def update_target_network(self):
        #target_state_dict=self.target_network.state_dict()
        main_state_dict=self.main_network.state_dict()
        #for key in main_state_dict:
            #target_state_dict[key]=main_state_dict[key]
        self.target_network.load_state_dict(main_state_dict)
        #self.target_network.weight = nn.Parameter(self.main_network.parameters())
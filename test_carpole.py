import random
import gym
import numpy as np
from collections import deque

from Agent_double import DQNAgent

ENV_NAME = "CartPole-v1"
batch_size = 1

def carpole(gamma, learning_rate, episodes, epsilon, buffer_len, batch_size):
    env = gym.make(ENV_NAME)
    
    observation_space = env.observation_space.shape[0]
    action_space = env.action_space.n
    dqn_solver = DQNAgent(observation_space, action_space, gamma=gamma, lr=learning_rate, epsilon=epsilon, buffer=buffer_len)
    episodes = int(episodes)
    run = 0
    final_score = 0
    #state, info = env.reset(seed=42)

    for i in range(episodes):
        run += 1
        state = env.reset()
        state = np.reshape(state[0], [1, observation_space])
        step = 0
        while True:
            losslist = []
            step += 1
            env.render()

            if step % dqn_solver.update_rate == 0:
                dqn_solver.update_target_network()

            action = dqn_solver.epsilon_greedy(state)
            
            state_next, reward, terminated, _, _ = env.step(int(action))
            if not terminated:
                reward += 0.1
            else:
                reward = reward - 1
            state_next = np.reshape(state_next, [1, observation_space])
            dqn_solver.store_transistion(state, action, reward, state_next, terminated)
            state = state_next
            if len(dqn_solver.replay_buffer) > batch_size:
                lossvalue = dqn_solver.train(batch_size)
                losslist.append(lossvalue.item())
            if terminated:
                
                #print("Run:" + str(run) + ", score: " + str(step))
                
                final_score = step
                break
        if i >=episodes-11:
            final_score += final_score  
        
    return int(final_score/10)    



if __name__ == "__main__":

    print(carpole(gamma=0.99, learning_rate=0.001, episodes=600, epsilon=0.4, buffer_len=1000, batch_size=64))
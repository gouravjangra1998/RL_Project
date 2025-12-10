import gymnasium as gym
from stable_baselines3 import PPO

# Create environment
env = gym.make("LunarLander-v3")

# Initialize PPO agent
model = PPO("MlpPolicy", env, verbose=1)

# Train agent
model.learn(total_timesteps=500_000)

# Save model
model.save("ppo_lunarlander")

import env_sar
import env_sar_mod

#env = env_sar.env(num_good=1, num_adversaries=7, num_obstacles=5, max_cycles=1000, continuous_actions=True, render_mode="human")
env = env_sar_mod.env(num_agents=1, num_hostages=2, num_goals=1, max_cycles=10000, continuous_actions=True, render_mode="human")


env.reset()

#print(env.num_agents)

for agent in env.agent_iter():
    print(agent)
    observation, reward, termination, truncation, info = env.last()

    if termination or truncation:
        action = None
    else:
        # this is where you would insert your policy
        action = env.action_space(agent).sample()

    env.step(action)
env.close()

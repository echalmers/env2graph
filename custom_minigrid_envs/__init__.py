from gymnasium.envs.registration import register

register(
    id='MiniGrid-Custom-TestEnv',
    entry_point='custom_minigrid_envs.envs:TestEnv',
)
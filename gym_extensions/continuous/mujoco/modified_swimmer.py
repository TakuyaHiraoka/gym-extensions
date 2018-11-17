import numpy as np
from gym import utils
from gym.envs.mujoco import mujoco_env
import os.path as osp
from gym_extensions.continuous.mujoco.wall_envs import MazeFactory

from gym.envs.mujoco.swimmer import SwimmerEnv

import os
import gym


SwimmerMaze = lambda *args, **kwargs : MazeFactory(ModifiedSwimmerEnv)(model_path=os.path.dirname(gym.envs.mujoco.__file__) + "/assets/swimmer.xml", ori_ind=0, *args, **kwargs)



class ModifiedSwimmerEnv(SwimmerEnv, utils.EzPickle):
    """
    Simply allows changing of XML file, probably not necessary if we pull request the xml name as a kwarg in openai gym
    """
    def __init__(self, **kwargs):
        mujoco_env.MujocoEnv.__init__(self, kwargs["model_path"], 4)
        utils.EzPickle.__init__(self)

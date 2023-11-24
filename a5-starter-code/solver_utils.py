#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Tuple, Callable, List

import math
import toh_mdp as tm


def value_iteration(
        mdp: tm.TohMdp, v_table: tm.VTable
) -> Tuple[tm.VTable, tm.QTable, float]:
    """Computes one step of value iteration.

    Hint 1: Since the terminal state will always have value 0 since
    initialization, you only need to update values for nonterminal states.

    Hint 2: It might be easier to first populate the Q-value table.

    Args:
        mdp: the MDP definition.
        v_table: Value table from the previous iteration.

    Returns:
        new_v_table: tm.VTable
            New value table after one step of value iteration.
        q_table: tm.QTable
            New Q-value table after one step of value iteration.
        max_delta: float
            Maximum absolute value difference for all value updates, i.e.,
            max_s |V_k(s) - V_k+1(s)|.
    """
    new_v_table: tm.VTable = v_table.copy()
    q_table: tm.QTable = {}
    # noinspection PyUnusedLocal
    max_delta = 0.0
    # *** BEGIN OF YOUR CODE ***
    for state in mdp.state_graph:
        q_max = -1 * math.inf
        for action in mdp.actions:
            q_sum = 0
            for next_state in mdp.all_states:
                q_sum += mdp.transition(state,action,next_state)*(mdp.reward(state,action,next_state)+(mdp.config.gamma*v_table[next_state]))
            q_table[state,action] = q_sum
            if q_table[state,action] > q_max:
                q_max = q_table[state,action]
        new_v_table[state] = q_max
        if abs(new_v_table[state]-v_table[state])>max_delta:
            max_delta = abs(new_v_table[state]-v_table[state])
    # ***  END OF YOUR CODE  ***
    return new_v_table, q_table, max_delta


def extract_policy(
        mdp: tm.TohMdp, q_table: tm.QTable
) -> tm.Policy:
    """Extract policy mapping from Q-value table.

    Remember that no action_state is available from the terminal state, so the
    extracted policy only needs to have all the nonterminal states (can be
    accessed by mdp.nonterminal_states) as keys.

    Args:
        mdp: the MDP definition.
        q_table: Q-Value table to extract policy from.

    Returns:
        policy: tm.Policy
            A Policy maps nonterminal states to actions.
    """
    # *** BEGIN OF YOUR CODE ***
    policy: tm.Policy = {}
    for state in mdp.nonterminal_states:
        best_q = -1 * math.inf
        for action in mdp.actions:
            if q_table[state,action]>best_q:
                policy[state] = action
                best_q = q_table[state,action]
    return policy


def q_update(
        mdp: tm.TohMdp, q_table: tm.QTable,
        transition: Tuple[tm.TohState, tm.TohAction, float, tm.TohState],
        alpha: float) -> None:
    """Perform a Q-update based on a (S, A, R, S') transition.

    Update the relevant entries in the given q_update based on the given
    (S, A, R, S') transition and alpha value.

    Args:
        mdp: the MDP definition.
        q_table: the Q-Value table to be updated.
        transition: A (S, A, R, S') tuple representing the agent transition.
        alpha: alpha value (i.e., learning rate) for the Q-Value update.
    """
    state, action_state, reward, next_state = transition
    # *** BEGIN OF YOUR CODE ***
    q_max = -1*math.inf
    for next_action in mdp.actions:
        if (next_state,next_action) in q_table.keys():
            q_max = q_table[next_state,next_action] if q_table[next_state,next_action]>q_max else q_max
    q_max = 0 if q_max == -1*math.inf else q_max
    q_table[state,action_state]=q_table[state,action_state]+alpha*(reward+(mdp.config.gamma*q_max)-q_table[state,action_state])


def extract_v_table(mdp: tm.TohMdp, q_table: tm.QTable) -> tm.VTable:
    """Extract the value table from the Q-Value table.

    Args:
        mdp: the MDP definition.
        q_table: the Q-Value table to extract values from.

    Returns:
        v_table: tm.VTable
            The extracted value table.
    """
    # *** BEGIN OF YOUR CODE ***
    v_table: tm.VTable = {}
    for state in mdp.nonterminal_states:
        q_max = -1*math.inf
        for action in mdp.actions:
            if (state,action) in q_table.keys():
                q_max = q_table[state,action] if q_table[state,action]>q_max else q_max
        v_table[state] = q_max
    return v_table


def choose_next_action(
        mdp: tm.TohMdp, state: tm.TohState, epsilon: float, q_table: tm.QTable,
        epsilon_greedy: Callable[[List[tm.TohAction], float], tm.TohAction]
) -> tm.TohAction:
    """Use the epsilon greedy function to pick the next action_state.

    You can assume that the passed in state is neither the terminal state nor
    any goal state.

    You can think of the epsilon greedy function passed in having the following
    definition:

    def epsilon_greedy(best_actions, epsilon):
        # selects one of the best actions with probability 1-epsilon,
        # selects a random action_state with probability epsilon
        ...

    See the concrete definition in QLearningSolver.epsilon_greedy.

    Args:
        mdp: the MDP definition.
        state: the current MDP state.
        epsilon: epsilon value in epsilon greedy.
        q_table: the current Q-value table.
        epsilon_greedy: a function that performs the epsilon

    Returns:
        action_state: tm.TohAction
            The chosen action_state.
    """
    # *** BEGIN OF YOUR CODE ***
    q_max = -1*math.inf
    best_actions = [tm.TohAction]
    for action in mdp.actions:
        if (state,action) in q_table.keys():
            if q_table[state,action]>=q_max:
                if q_table[state,action]>q_max:
                    best_actions.clear()
                    q_max = q_table[state,action]
                best_actions.append(action)
    return epsilon_greedy(best_actions, epsilon)


def custom_epsilon(n_step: int) -> float:
    """Calculates the epsilon value for the nth Q learning step.

    Define a function for epsilon based on `n_step`.

    Args:
        n_step: the nth step for which the epsilon value will be used.

    Returns:
        epsilon: float
            epsilon value when choosing the nth step.
    """
    # *** BEGIN OF YOUR CODE ***
    return n_step


def custom_alpha(n_step: int) -> float:
    """Calculates the alpha value for the nth Q learning step.

    Define a function for alpha based on `n_step`.

    Args:
        n_step: the nth update for which the alpha value will be used.

    Returns:
        alpha: float
            alpha value when performing the nth Q update.
    """
    # *** BEGIN OF YOUR CODE ***

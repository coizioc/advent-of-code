from __future__ import annotations
from dataclasses import dataclass, field
import functools
import re
from typing import List

with open("input/year2022/day19.txt", "r") as f:
    lines = f.read().splitlines()

class Blueprint:
    costs: List[List[int]]

    def __init__(
        self,
        ore_ore_cost: int,
        clay_ore_cost: int,
        obsidian_ore_cost: int,
        obsidian_clay_cost: int,
        geode_ore_cost: int,
        geode_obsidian_cost: int,
    ):
        self.costs = []
        self.costs.append([ore_ore_cost, 0, 0, 0])
        self.costs.append([clay_ore_cost, 0, 0, 0])
        self.costs.append([obsidian_ore_cost, obsidian_clay_cost, 0, 0])
        self.costs.append([geode_ore_cost, 0, geode_obsidian_cost, 0])

    def try_buy_robot(self, type_idx: int, materials, robots):
        # Always buy geode robots if we can.
        if type_idx == 3 and self.can_buy_robot(materials, type_idx):
            return [
                material - cost
                for material, cost in zip(materials, self.costs[type_idx])
            ], [x + 1 if i == type_idx else x for i, x in enumerate(robots)]
        # Otherwise, only try to buy a robot if we cannot produce it within a single turn.
        if self.can_buy_robot(
            materials, type_idx
        ) and self.robot_cannot_be_produced_in_one_turn(robots, type_idx):
            return [
                material - cost
                for material, cost in zip(materials, self.costs[type_idx])
            ], [x + 1 if i == type_idx else x for i, x in enumerate(robots)]
        return None, None

    def can_buy_robot(self, materials, type_idx: int):
        return all(
            material - cost >= 0
            for material, cost in zip(materials, self.costs[type_idx])
        )

    def robot_cannot_be_produced_in_one_turn(self, robots, type_idx: int):
        return max(cost[type_idx] for cost in self.costs) > robots[type_idx]

    def __hash__(self):
        return hash(str(self.costs))


@dataclass
class MiningState:
    blueprint: Blueprint

    time: int = 0

    # [ore, clay, obsidian, geode]
    materials: List[int] = field(default_factory=lambda: [0, 0, 0, 0])
    robots: List[int] = field(default_factory=lambda: [1, 0, 0, 0])

    def next_states(self) -> List[MiningState]:
        states = []

        # Add a state for doing nothing.
        states.append(
            MiningState(
                self.blueprint,
                self.time + 1,
                [sum(x) for x in zip(self.materials, self.robots)],
                self.robots,
            )
        )

        # Add a state for each possible purchase.
        for i in range(3, -1, -1):
            new_materials, new_robots = self.blueprint.try_buy_robot(
                i, self.materials, self.robots
            )
            if new_materials is not None:
                states.append(
                    MiningState(
                        self.blueprint,
                        self.time + 1,
                        [sum(x) for x in zip(new_materials, self.robots)],
                        new_robots,
                    )
                )

        return states

    def __hash__(self) -> int:
        return hash((self.blueprint, str(self.materials), str(self.robots)))


blueprints = []
for line in lines:
    match = re.match(
        r"Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.",
        line,
    )
    # ore_cost, clay_cost, obsidian_ore_cost, obsidian_clay_cost, geode_ore_cost, geode_obsidian_cost
    blueprints.append(Blueprint(*[int(x) for x in match.groups()]))


def get_max_geodes(n_mins: int, blueprint: Blueprint) -> int:
    initial_state = MiningState(blueprint)
    states_to_visit = [initial_state]
    curr_max_geodes = 0
    visited_states = set()

    while len(states_to_visit) > 0:
        state = states_to_visit.pop()
        if state in visited_states:
            continue

        visited_states.add(state)

        if state.time > n_mins:
            if state.materials[3] > curr_max_geodes:
                curr_max_geodes = state.materials[3]
        else:
            # Only consider state if we can possibly beat our current maximum.
            remaining_time = n_mins - state.time
            max_geodes_produced_by_existing_robots = state.robots[3] * remaining_time
            max_geodes_produces_by_new_robots = (
                remaining_time * (remaining_time - 1) / 2
            )

            if (
                max_geodes_produces_by_new_robots
                + max_geodes_produced_by_existing_robots
                + state.materials[3]
                > curr_max_geodes
            ):
                states_to_visit.extend(state.next_states())
    return curr_max_geodes


max_geodes_per_blueprint = [get_max_geodes(24, blueprint) for blueprint in blueprints]
print(sum((i + 1) * max_geodes for i, max_geodes in enumerate(max_geodes_per_blueprint)))

max_geodes_per_blueprint = [
    get_max_geodes(32, blueprint) for blueprint in blueprints[:3]
]
print(functools.reduce(lambda x, y: x * y, max_geodes_per_blueprint))

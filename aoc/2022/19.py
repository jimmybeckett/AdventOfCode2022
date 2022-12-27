# with open('scratch2.txt') as f:
import re

from tqdm import tqdm
 




def geodes(robot_costs, robots, resources, minutes):
    # base case
    if minutes == 0:
        return resources['geode']

    # produce
    old_resources = resources.copy()
    for resource, production in robots.items():
        resources[resource] += production

    if old_resources['ore'] >= robot_costs['geode']['ore'] \
            and old_resources['obsidian'] >= robot_costs['geode']['obsidian']:
        robots['geode'] += 1
        resources['ore'] -= robot_costs['geode']['ore']
        resources['obsidian'] -= robot_costs['geode']['obsidian']
        return geodes(robot_costs, robots, resources, minutes - 1)
    else:
        candidates = []

        # attempt to build an obsidian robot
        if old_resources['ore'] >= robot_costs['obsidian']['ore'] \
                and old_resources['clay'] >= robot_costs['obsidian']['clay']\
                and robots['obsidian'] < robot_costs['geode']['obsidian']:
            # choose
            robots['obsidian'] += 1
            resources['ore'] -= robot_costs['obsidian']['ore']
            resources['clay'] -= robot_costs['obsidian']['clay']
            # explore
            candidates.append(geodes(robot_costs, robots, resources, minutes - 1))
            # unchoose
            robots['obsidian'] -= 1
            resources['ore'] += robot_costs['obsidian']['ore']
            resources['clay'] += robot_costs['obsidian']['clay']

        # attempt to build a clay robot
        if old_resources['ore'] >= robot_costs['clay']['ore']\
                and robots['clay'] < robot_costs['obsidian']['clay']:
            # choose
            robots['clay'] += 1
            resources['ore'] -= robot_costs['clay']['ore']
            # explore
            candidates.append(geodes(robot_costs, robots, resources, minutes - 1))
            # unchoose
            robots['clay'] -= 1
            resources['ore'] += robot_costs['clay']['ore']

        # attempt to build a ore robot
        if old_resources['ore'] >= robot_costs['ore']['ore']:
            # choose
            robots['ore'] += 1
            resources['ore'] -= robot_costs['ore']['ore']
            # explore
            candidates.append(geodes(robot_costs, robots, resources, minutes - 1))
            # unchoose
            robots['ore'] -= 1
            resources['ore'] += robot_costs['ore']['ore']
        candidates.append(geodes(robot_costs, robots, resources, minutes - 1))
        for resource, production in robots.items():
            resources[resource] -= production
        return max(candidates)


# def geodes(robot_costs, robots, resources, minutes):


with open('scratch2.txt') as f:
    for blueprint in f:
        robots = dict(ore=1, clay=0, obsidian=0, geode=0)
        resources = dict(ore=0, clay=0, obsidian=0, geode=0)
        robot_costs = dict()
        s = blueprint.split('.')
        ore_costs = re.findall(r'\d+', s[0])
        blueprint_id = int(ore_costs[0])
        robot_costs['ore'] = dict(ore=int(ore_costs[1]))
        robot_costs['clay'] = dict(ore=int(re.search(r'\d+', s[1]).group()))
        obsidian_costs = re.findall(r'\d+', s[2])
        robot_costs['obsidian'] = dict(ore=int(obsidian_costs[0]), clay=int(obsidian_costs[1]))
        geode_costs = re.findall(r'\d+', s[3])
        robot_costs['geode'] = dict(ore=int(geode_costs[0]), obsidian=int(geode_costs[1]))
        print(geodes(robot_costs, robots, resources, 19))
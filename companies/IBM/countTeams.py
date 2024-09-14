from typing import List
import itertools


def countTeams(skills: List[int], minPlayers: int, minLevel: int, maxLevel: int) -> int:
    """
    Counts the number of valid teams that can be formed based on player skill levels and constraints.

    Args:
        skills (List[int]): List of skill levels for each player.
        minPlayers (int): Minimum number of players required for a valid team.
        minLevel (int): Minimum skill level allowed for a player to be part of a team.
        maxLevel (int): Maximum skill level allowed for a player to be part of a team.

    Returns:
        int: The number of valid teams that can be formed.
    """

    filter_skills = [level for level in skills if minLevel <= level <= maxLevel]
    count = 0

    for i in range(minPlayers, len(filter_skills) + 1):
        combos = itertools.combinations(filter_skills, i)
        count += len(list(combos))
    return count


if __name__ == "__main__":
    skills = [12, 4, 6, 13, 5, 10]
    minPlayers = 3
    minLevel = 4
    maxLevel = 10
    print(countTeams(skills, minPlayers, minLevel, maxLevel))  # 5

    skills = [4, 8, 5, 6]
    minPlayers = 2
    minLevel = 10
    maxLevel = 20
    print(countTeams(skills, minPlayers, minLevel, maxLevel))  # 0

    skills = [1, 2, 3, 4]
    minPlayers = 4
    minLevel = 1
    maxLevel = 6
    print(countTeams(skills, minPlayers, minLevel, maxLevel))  # 1

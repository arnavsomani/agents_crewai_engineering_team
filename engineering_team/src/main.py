#!/usr/bin/env python
from engineering_team.crew import EngineeringTeamCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    EngineeringTeamCrew().crew().kickoff(inputs=inputs)
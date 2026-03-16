from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class EngineeringTeamCrew():
	"""EngineeringTeam crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'


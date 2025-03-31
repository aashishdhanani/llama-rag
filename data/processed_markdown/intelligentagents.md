## Intelligent Agents

Chapter 2

## Outline

- · Agents and environments
- · Rationality
- · PEAS (Performance measure, Environment, Actuators, Sensors)
- · Environment types
- · Agent types

## Agent and Env

- · An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators.
- · The agent function maps from percept histories to actions:

<!-- image -->

<!-- formula-not-decoded -->

## Agents

- · An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators.

<!-- image -->

Human agent:

eyes, ears, and other organs for sensors.

hands, legs, mouth, and other body parts for actuators.

Robotic agent:

cameras and infrared range finders for sensors.

various motors for actuators.

Software agent:

keyboard inputs, reading from files, network signals Screen output, writing to files, network outputs

## Vacuum-cleaner world

<!-- image -->

## Vacuum-cleaner world

<!-- image -->

- •
- Percepts: location and contents, e.g., [A,Dirty]
- · Actions:

Left , Right , Suck

- · Function-table (table look-up agent)
- •Huge table.
- •Take a long time to build
- the table.
- •No autonomy.
- ·Even with learning, need a long time to learn the table entries.

| Percept                                     | Action               |
|---------------------------------------------|----------------------|
| [A, Clean] [A, Dirty] [B, Clean] [B, Dirty] | Right Suck Left Suck |

## Rational agents

- · An agent should strive to "do the right thing", based on what it can perceive and the actions it can perform. The right action is the one that will cause the agent to be most successful.
- · Performance measure: An objective criterion for success of an agent's behavior.

## Rational agents

- · Rational Agent: For each possible percept sequence, a rational agent should select an action that is expected to maximize its performance measure, given the evidence provided by the percept sequence and whatever built-in knowledge the agent has.
- - The performance measure that defines the criterion of success.
- - The agent's prior knowledge of the environment.
- - The actions that the agent can perform.
- - The agent's percept sequence to date.

## Is a Vacuum-Cleaner Agent Rational?

<!-- image -->

- · Depends!
- · Performance measure

## Is a Vacuum-Cleaner Agent Rational?

- -amount of dirt cleaned up,
- -amount of time taken,
- -amount of electricity consumed,
- -amount of noise generated, etc..
- · A priori
- -Geography of the environment is known (two squares, A is on left and B is on right, etc.).
- -Perception is trustable (no illusion).
- -Sucking cleans the current square (no dysfunctional).
- · Actions
- -Left, right, suck.
- · Current percept
- -[location, dirt]
- · Possibilities
- -Penalty to each movement.
- -The agent have memory (reasoning percept histories).
- -The geography of the environment is unknown.
- -Clean square can become dirty.
- -The agent cannot percept its current location.
- -Agent can learn from experience.

## Specify the setting for intelligent agent design: PEAS Description

- · PEAS: Performance measure, Environment, Actuators, Sensors
- · Eg1. Automated taxi driver (open-end research of Intelligent Transportation Systems)
- · Eg2. Medical diagnosis system
- · Eg3. Part-picking robot
- · Eg4. Interactive English tutor

## Specify the setting for intelligent agent design: PEAS Description

- · PEAS: Performance measure, Environment, Actuators, Sensors
- · Eg1. Automated taxi driver (open-end research of Intelligent Transportation Systems):
- - Performance measure: Safe, fast, legal, comfortable trip, maximize profits.
- - Environment: Roads, other traffic, pedestrians, customers.
- - Actuators: Steering wheel, accelerator, brake, signal, horn.
- - Sensors: Cameras, sonar, speedometer, GPS, odometer, engine sensors, keyboard.

## PEAS

- · Eg2. Medical diagnosis system
- - Performance measure: Healthy patient, minimize costs, lawsuits.
- - Environment: Patient, hospital, staff
- - Actuators: Screen display (questions, tests, diagnoses, treatments, referrals).
- - Sensors: Keyboard (entry of symptoms, findings, patient's answers).

## PEAS

- · Eg3. Part-picking robot
- - Performance measure: Percentage of parts in correct bins.
- - Environment: Conveyor belt with parts, bins.
- - Actuators: Jointed arm and hand.
- - Sensors: Camera, joint angle sensors.

## PEAS

- · Eg4. Interactive English tutor
- - Performance measure: Maximize student's score on test.
- - Environment: Set of students.
- - Actuators: Screen display (exercises, suggestions, corrections).

- Sensors: Keyboard.

## Environment types

- · Fully observable (vs. partially observable): An agent can access the complete state of the environment at each point in time.
- -Do not maintain the internal state to keep track of the world.
- · Deterministic (vs. stochastic): The next state of the environment is completely determined by the current state and the action executed by the agent.
- -Do not worry about uncertainty.
- · Episodic (vs. sequential): An agent's action depends only on an 'episode' (snapshot) of the environment, i.e. history independent.
- -Do not think ahead.

## Environment types

- · Fully observable (vs. partially observable): An agent can access the complete state of the environment at each point in time.
- -Do not maintain the internal state to keep track of the world.
- · Deterministic (vs. stochastic): The next state of the environment is completely determined by the current state and the action executed by the agent.
- -Do not worry about uncertainty.

- Playing chess?

Fully.

- Medical diagnosis?

Partially.

- Taxi driving?

Partially.

- Playing chess?

Deterministic.

- Medical diagnosis?

Stochastic.

- Battle field?

Stochastic.

- E-shopping?

Deterministic.

- E-auction?

Stochastic.

## Environment types

- · Episodic (vs. sequential): An agent's action depends only on an 'episode' (snapshot) of the environment, i.e. history independent.
- - Do not think ahead.

- Medical diagnosis?

Sequential.

- Web search?

Episodic.

- E-shopping?

Episodic.

## Environment types

- · Dynamic (vs. static): The environment changes over time beyond the agent's control.
- - Do not keep looking at env when making decisions.
- · Discrete (vs. continuous): A limited number of distinct, clearly defined percepts and actions.
- · Single agent (vs. multi-agent): An agent operating by itself in an environment.

## Environment types

- · Dynamic (vs. static): The environment changes over time beyond the agent's control.
- - Playing crossword puzzle?  Static.
- - Expert systems? Static.
- - Playing chess?

Semi-dynamic.

- - Playing soccer?

Dynamic.

- - Battle field?

Dynamic.

- - Do not keep looking at env when making decisions.
- · Discrete (vs. continuous): A limited number of distinct, clearly defined percepts and actions.

- Playing chess?

Discrete.

- Taxi driving?

Continuous.

## Environment types

- · Single agent (vs. multi-agent): An agent operating by itself in an environment.
- - Crossword puzzle? Single
- - Playing chess? Multi.
- - Taxi driving? Multi.
- · Which is harder?
- · The environment type largely determines the agent design.
- · The real world is partially observable, stochastic, sequential, dynamic, continuous, multi-agent.

## Agent Types

- · Simple reflex agents
- · Model-based reflex agents
- · Goal-based agents
- · Utility-based agents

<!-- image -->

## Simple reflex agents

<!-- image -->

Use condition-action rules to map the agent's perceptions directly to action.

Making decisions only with inputs.

## Model-based reflex agents

<!-- image -->

Have an internal model (state) of the external environment.

## Goal-based agents

<!-- image -->

## Utility-based agents

<!-- image -->

## Technologies of Software Agents

- · Machine learning
- · Information retrieval
- · Agent communication
- · Agent coordination
- · Agent negotiation
- · Natural language understanding
- · Distributed objects
from .. import Events, State, Supervisor

# Create states
G2S0_E1S0_E2S0_state = State("G2S0_E1S0_E2S0", True)
G2S0_E1S1_E2S0_state = State("G2S0_E1S1_E2S0", False)
G2S0_E1S1_E2S1_state = State("G2S0_E1S1_E2S1", False)
G2S1_E1S0_E2S0_state = State("G2S1_E1S0_E2S0", False)
G2S1_E1S0_E2S1_state = State("G2S1_E1S0_E2S1", False)
G2S1_E1S1_E2S0_state = State("G2S1_E1S1_E2S0", False)
G2S1_E1S1_E2S1_state = State("G2S1_E1S1_E2S1", False)


# Create transitions
G2S0_E1S0_E2S0_state.add_transition(Events['btn'], G2S0_E1S1_E2S1_state)
G2S0_E1S1_E2S0_state.add_transition(Events['btn'], G2S0_E1S1_E2S1_state)
G2S0_E1S1_E2S0_state.add_transition(Events['liga'], G2S1_E1S0_E2S0_state)
G2S0_E1S1_E2S1_state.add_transition(Events['btn'], G2S0_E1S1_E2S0_state)
G2S0_E1S1_E2S1_state.add_transition(Events['liga'], G2S1_E1S0_E2S1_state)
G2S1_E1S0_E2S0_state.add_transition(Events['desliga'], G2S0_E1S0_E2S0_state)
G2S1_E1S0_E2S0_state.add_transition(Events['btn'], G2S1_E1S1_E2S1_state)
G2S1_E1S0_E2S1_state.add_transition(Events['btn'], G2S1_E1S1_E2S0_state)
G2S1_E1S1_E2S0_state.add_transition(Events['desliga'], G2S0_E1S1_E2S0_state)
G2S1_E1S1_E2S0_state.add_transition(Events['btn'], G2S1_E1S1_E2S1_state)
G2S1_E1S1_E2S1_state.add_transition(Events['btn'], G2S1_E1S1_E2S0_state)


# create state list
state_list = []
state_list.append(G2S0_E1S0_E2S0_state)
state_list.append(G2S0_E1S1_E2S0_state)
state_list.append(G2S0_E1S1_E2S1_state)
state_list.append(G2S1_E1S0_E2S0_state)
state_list.append(G2S1_E1S0_E2S1_state)
state_list.append(G2S1_E1S1_E2S0_state)
state_list.append(G2S1_E1S1_E2S1_state)


# create event list
alphabet = []
alphabet.append(Events['btn'])
alphabet.append(Events['liga'])
alphabet.append(Events['desliga'])


# create supervisor
sup = Supervisor("sup", state_list, alphabet)
from events import Events
from State import State
from Supervisor import Supervisor

# Create states
%$%{states}

# Create transitions
%$%{transitions}

# create state list
state_list = []
%$%{state_list}

# create event list
alphabet = []
%$%{alphabet}

# create supervisor
%$%supervisor_name = Supervisor("%$%supervisor_name", state_list, alphabet)
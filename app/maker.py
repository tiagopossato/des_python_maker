from bs4 import BeautifulSoup 
import os
import argparse
from string import Template

class CustomTemplate(Template):
	delimiter = '%$%'

def fill_template(template, dest, template_dict):
    # verify if scrtip is being executed on windows and convert paths to windows format
    if os.name == 'nt':
        template = template.replace('/', '\\')
        dest = dest.replace('/', '\\')
    
    # make the names of the files
    with open(template, 'r') as f:
        src = CustomTemplate(f.read())
        result = src.safe_substitute(template_dict)

    arquivo = open(dest,'w')
    arquivo.write(result)
    arquivo.close()


base_dir = os.path.dirname(os.path.realpath(__file__))


parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, help='Input file')
parser.add_argument('--output', type=str, help='Output path')

input = parser.parse_args().input
output_dir = parser.parse_args().output

if input==None or not os.path.exists(input):
    print(f"File {input} not found")
    exit(-1)

# print input and output files
print(f"Input file: {input}")
print(f"Output path: {output_dir}")

# open file
with open(input, 'r') as f:
    data = f.read() 

# parse file with BeautifulSoup
bs_data = BeautifulSoup(data, "xml")

# get all Events
event_decl_list = bs_data.find_all('EventDeclList')
event_list = []
for e in event_decl_list[0].find_all('EventDecl'):
    if(e.get('Kind') == 'PROPOSITION'):
        continue
    event_list.append({'Kind':e.get('Kind'), 'Name':e.get('Name')})


# get all supervisors
simple_component_supervisor = bs_data.find_all('SimpleComponent', {'Kind':'SUPERVISOR'})

# get all simple components with kind Plant wich starts with 'GD'
simple_component_plant = bs_data.find_all('SimpleComponent', {'Kind':'PLANT'})
simple_component_plant = [x for x in simple_component_plant if x.get('Name').startswith('GD')]
simple_component_supervisor = simple_component_supervisor + simple_component_plant

supervisors = []
for supervisor in simple_component_supervisor:
    sup = {}
    sup['name'] = supervisor.get('Name')

    if(len(supervisor.find_all('NodeList')) > 1):
        print(f"Error: multiple NodeList on Supervisor {sup['name']}")
        exit(-1)
    state_list = []
    for node in supervisor.find_all('NodeList')[0].find_all('SimpleNode'):
        state_list.append({'Name':node.get('Name'), 'Initial': 1 if node.get('Initial')!=None else 0})
    sup['state_list'] = state_list

    edgeList = supervisor.find_all('EdgeList')[0].find_all('Edge')
    # if(len(EdgeList) > 1):
    #     print(f"Error: multiple EdgeList on Supervisor {sup['name']}")
    #     exit(-1)
    # order edgeList by Source
    edgeList = sorted(edgeList, key=lambda k: k.get('Source'))

    transition_list = []
    local_event_list = []
    for node in edgeList:
        for evt in node.find_all('SimpleIdentifier'):
            transition_list.append({'Source':node.get('Source'), 'Event':evt.get('Name'), 'Target':node.get('Target')})
            for x in event_list:
                if x['Name'] == evt.get('Name'):
                    e = {'Kind':x['Kind'], 'Name':evt.get('Name')}
                    if(e not in local_event_list):
                        local_event_list.append(e)
                    break
    sup['transition_list'] = transition_list
    sup['event_list'] = local_event_list
    supervisors.append(sup)


# make file events_names.py
# 'Se': Event(EventKind.UNCONTROLLABLE, 0, "Se"),
events = ""

# create set callback list
# Events['Se'].set_callback(default_callback)
set_callback = ""

# create handle events list for test
# handle_event(Events['Se'])
handle_event = ""

i = 0
for event in event_list:
    event['Name'] = event['Name'].replace('.', '_')
    events += f"    '{event['Name']}': Event(EventKind.{event['Kind']}, {i}, '{event['Name']}'),\n"
    set_callback += f"Events['{event['Name']}'].set_callback(default_callback)\n"
    handle_event += f"    handle_event(Events['{event['Name']}'])\n"
    i = i + 1

fill_template(f"{base_dir}/template/Supervisor/events-template.py",
                f"{output_dir}/Supervisor/events.py", 
                {'events': events})

fill_template(f"{base_dir}/template/main-template.py",
                f"{output_dir}/main.py", 
                {'set_callback': set_callback,
                'handle_event': handle_event})

# create import list
import_list = ""

# create supervisor list for use in handle_event
supervisor_list = ""

for sup in supervisors:
    import_list += f"from .{sup['name']} import {sup['name']}\n"
    supervisor_list += f"{sup['name']},"
    # Create states
    # q0_state = State("q0", True)
    states = ""
    for state in sup['state_list']:
        # change . to _ in state name
        state['Name'] = state['Name'].replace('.', '_')
        states += f"{state['Name']}_state = State(\"{state['Name']}\", {True if state['Initial']==1 else False})\n"

    # Create transitions
    # q0_state.add_transition(Events['btnON'], q3_state)
    transitions = ""
    for transition in sup['transition_list']:
        # change . to _ in transition  Source name
        transition['Source'] = transition['Source'].replace('.', '_')
        # change . to _ in transition  Target name
        transition['Target'] = transition['Target'].replace('.', '_')
        transitions += f"{transition['Source']}_state.add_transition(Events['{transition['Event']}'], {transition['Target']}_state)\n"

    # create event list
    # event_list.append(btnON_evt)
    alphabet = ""
    for event in sup['event_list']:
        alphabet += f"alphabet.append(Events['{event['Name']}'])\n"

    # create state list
    # state_list.append(q0_state)
    state_list = ""
    for state in sup['state_list']:
        state_list += f"state_list.append({state['Name']}_state)\n"

    # create supervisor file
    fill_template(f"{base_dir}/template/Supervisor/supervisors/supervisor-template.py",
                f"{output_dir}/Supervisor/supervisors/{sup['name']}.py",
                {'events': events,
                'states': states,
                'transitions': transitions,
                'alphabet': alphabet,
                'state_list': state_list,
                'supervisor_name': sup['name']})

fill_template(f"{base_dir}/template/Supervisor/supervisors/__init__-template.py",
                f"{output_dir}/Supervisor/supervisors/__init__.py", 
                {'import_list': import_list})

# remove last comma
supervisor_list = supervisor_list[:-1]
fill_template(f"{base_dir}/template/Supervisor/__init__-template.py",
                f"{output_dir}/Supervisor/__init__.py", 
                {'supervisor_list': supervisor_list})


# print("Lista de eventos:")
# print(event_list)

# # print supervisor in readable format
# for sup in supervisors:
#     print(f"Supervisor {sup['name']}:")
#     print(f"\tEvents:")
#     for event in sup['event_list']:
#         print(f"\t\t{event['Name']}")
#     print(f"\tStates:")
#     for state in sup['state_list']:
#         print(f"\t\t{state['Name']}")
#     print(f"\tTransitions:")
#     for transition in sup['transition_list']:
#         print(f"\t\t{transition['Source']} -> {transition['Event']} -> {transition['Target']}")
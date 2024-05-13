SERVER_NAMES= []
SERVER_NAMES.append('Isaac and Glade')
SERVER_NAMES.append('Server for my friends')
SERVER_NAMES.append('Bob')
REACTION_ROLES = []
REACTION_ROLES_1 = ['Isaac and Glade', '🎉', 'Test Role', '🥺', 'Test Role 2', '😞', 'Um. This is a test role']
REACTION_ROLES_2 = ['Server for my friends', '☺️', 'Red', '🎉', 'Purple', '😢', 'Green']
REACTION_ROLES_3 = ['Bob', '☺️', 'Blue', '🎉', 'Orange', '😢', 'Yellow']

print(SERVER_NAMES)

def write_reaction_roles(server_name):
  reaction_roles_local = []
  if server_name == 'Isaac and Glade':
    reaction_roles_local = REACTION_ROLES_1
  elif server_name == 'Server for my friends':
    reaction_roles_local = REACTION_ROLES_2
  else:
    reaction_roles_local = REACTION_ROLES_3
  with open(f'./StuffForKeeping/reactionroles/{server_name}_reaction_roles.txt', 'a') as file:
    for roles in reaction_roles_local:
      file.write(f"{roles}\n")

def get_reaction_roles(server_name):
  reaction_roles_local = []
  with open(f'./StuffForKeeping/reactionroles/{server_name}_reaction_roles.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      reaction_roles_local.append(line.strip())
    REACTION_ROLES.append(reaction_roles_local)

for server in SERVER_NAMES:
  get_reaction_roles(server)      


print(REACTION_ROLES)


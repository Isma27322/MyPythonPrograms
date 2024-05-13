REACTION_ROLES = [['Server for my friends', '<:PandaPopcorn:1138522361482706954>', 'Pink', '🤨', 'Blue', '<:RedpandaHello:1203452427668426863>', 'Announcement Pings', '<:PandaCry:1138521808107221004>', 'Green', '🔥', 'Purple', '👍', 'Test Role'], ['Isaac and Glade', '🙂', 'Test Role 3', '🎉', 'Test role 4', '<:RedpandaHello:1203452427668426863>', 'Test Role', '😤', 'Test Role 2', '<:PandaRage:1138521977620013137>', 'Um. This is a test role']]
server_name = "Server for my friends"
foundNameAlready = False
serverindex = 0

print(REACTION_ROLES)

for role_for in REACTION_ROLES:  # Iterate directly through REACTION_ROLES
    if role_for[0] == server_name:  # Check only the first element of each inner list
        foundNameAlready = True
        serverindex = REACTION_ROLES.index(role_for)
        break
    else:
      foundNameAlready = False

print(foundNameAlready)

if foundNameAlready: 
   REACTION_ROLES[serverindex].append("test")

print(REACTION_ROLES)
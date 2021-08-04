import discord
import random
import os
import traceback

# 煽りメッセージ
aori_g = ["おっと、どうやらまだまだ練習が必要のようですね。","打ち間違えでしょうか、聞き間違えでしょうか。","すみません、今すごく笑ってますよ。なぜなら、あなたはこのコマンドを理解していないから。","えっと、それよりも先に誰かに/helpでも実行してもらうというのはいかがでしょうか。","もしかして、サーバーを間違えたのかな？","単純にしたつもりですが・・・。","実は私には特定のメッセージを消す権限があるのです。だから、本当はあなたのコマンドミスをなかったことにしたいけれど・・・。"]

token = os.environ['DISCORD_BOT_TOKEN']

# 起動時に動作する処理
#@client.event
#async def on_ready():
#    # 起動したらターミナルにログイン通知が表示される
#    print('ログインしました')

async def warn(message,guild,reason1,reason2):
    if (message.author.guild_permissions.administrator) == False:
        await message.channel.send('権限を持ってから実行しましょう。')
        return
    member = message.mentions[0]
    if len((member.roles)) >= 2:
        # すでにwarnされていたらkick
        for i in range(len(member.roles)):
            if member.roles[i].id == 871975827758252042:
                await member.kick(reason="/warn によるwarn2回目")
                embed=discord.Embed(title="kick!", color=0xff6666)
                embed.add_field(name=member.name+" キックされる", value=reason2, inline=False)
                await message.channel.send(embed=embed)
                return
            # warnguardの処理
            elif member.roles[i].id == 872005759045619732:
                role = guild.get_role(872005759045619732)
                await member.remove_roles(role)
                embed=discord.Embed(title="warnguard!", color=0xff66ff)
                embed.add_field(name=member.name+" が警告ガード！", value="warnが無効化されました！しかし、 "+member.name+" のwarnguardは壊れてしまいました・・・", inline=False)
                await message.channel.send(embed=embed)
                return
    role = guild.get_role(871975827758252042)
    await member.add_roles(role)
    embed=discord.Embed(title="warn!", color=0xffff66)
    embed.add_field(name=member.name+" へ警告", value=reason1, inline=False)
    await message.channel.send(embed=embed)

async def skick(message,guild,reason1,reason2):
    if (message.author.guild_permissions.administrator) == False:
        await message.channel.send('権限を持ってから実行しましょう。')
        return
    member = message.mentions[0]
    await member.kick(reason=reason2)
    embed=discord.Embed(title="kick!", color=0xff6666)
    embed.add_field(name=member.name+" キックされる", value=reason1, inline=False)
    await message.channel.send(embed=embed)

async def sban(message,guild,reason1,reason2):
    if (message.author.guild_permissions.administrator) == False:
        await message.channel.send('権限を持ってから実行しましょう。')
        return
    member = message.mentions[0]
    await member.ban(reason=reason2)
    embed=discord.Embed(title="BAN!", color=0xff0000)
    embed.add_field(name=member.name+" 参加禁止処分受ける", value=reason1, inline=False)
    await message.channel.send(embed=embed)


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    for i in range(len(message.author.roles)):
        if (message.author.roles)[i].id == 872093509035913216:
            await message.delete()
    # 「/help」と発言したらコマンド一覧が出る処理
    if message.content == '/help':
        embed=discord.Embed(title="コマンド一覧", color=0x2266ff)
        embed.add_field(name="/help", value="コマンド一覧を表示するほか、それぞれの説明、構文を表示します。", inline=False)
        embed.add_field(name="/strs2", value="Strs2", inline=False)
        embed.add_field(name="/dice [数字] [振る回数(省略可)]", value="サイコロを指定された条件下で振ります。", inline=False)
        embed.add_field(name="/search @[名前]", value="メンションした人の情報を取得し表示します。", inline=False)
        embed.add_field(name="/kickme", value="自分をキックします。権限者のみ使用不可", inline=False)
        embed.add_field(name="/banme", value="自分をBANします。権限者のみ使用不可", inline=False)
        embed.add_field(name="/kick @[名前]", value="メンションした人をキックします。権限者のみ使用可能", inline=False)
        embed.add_field(name="/ban @[名前]", value="メンションした人をBANします。権限者のみ使用可能", inline=False)
        embed.add_field(name="/warn @[名前]", value="メンションした人をwarnします。権限者のみ使用可能", inline=False)
        embed.add_field(name="/unwarn @[名前]", value="メンションした人のwarnを取り消します。権限者のみ使用可能", inline=False)
        embed.add_field(name="/guard @[名前]", value="メンションした人にwarnguardを付与します。権限者のみ使用可能", inline=False)
        embed.add_field(name="/mute @[名前]", value="メンションした人をミュートします。権限者のみ使用可能", inline=False)
        embed.add_field(name="/unmute @[名前]", value="メンションした人のミュートを解除します。権限者のみ使用可能", inline=False)
        embed.add_field(name="/clear", value="チャンネル内のすべてのログを消去します。権限者のみ使用可能", inline=False)
        await message.channel.send(embed=embed)
    # 「/strs2」と発言したら「strs2」が返る処理
    if message.content == '/strs2':
        embed=discord.Embed(title="Strs2", color=0xff0000)
        embed.add_field(name="Strs2", value="Strs2", inline=False)
        await message.channel.send(embed=embed)
    # 「/dice [数字]」と発言したら「[1から数字]」が返る処理
    if message.content.startswith('/dice'):
        if len(message.content.split()) == 1:
            await message.channel.send(random.choice(aori_g)+'/dice の構文は```/dice [面の数] [振る回数(省略可)]```です。')
            return
        if len(message.content.split()) == 2:
            await message.channel.send(random.randint(1,int((message.content.split())[1])))
            return
        dicelist=list(range(int((message.content.split()[2]))))
        for i in range(int((message.content.split()[2]))):
            dicelist[i]=random.randint(1,int((message.content.split())[1]))
        await message.channel.send(str(len(dicelist))+'回振った結果・・・'+str(','.join([str(n) for n in dicelist])))
    # 管理者以外が「/kickme」と発言したらキックされる処理
    if message.content == '/kickme':
        if message.author.guild_permissions.administrator:
            await message.channel.send('権限者は実行できません。')
            return
        member = message.author
        await member.kick(reason="/kickme によるkick")
        embed=discord.Embed(title="kick!", color=0xff6666)
        embed.add_field(name=member.name+" キックされる", value="/kickme によってkickされました。", inline=False)
        await message.channel.send(embed=embed)
    # 管理者以外が「/banme」と発言したらキックされる処理
    if message.content == '/banme':
        if message.author.guild_permissions.administrator:
            await message.channel.send('権限者は実行できません。')
            return
        member = message.author
        await member.ban(reason="/banme によるban")
        embed=discord.Embed(title="ban!", color=0xff0000)
        embed.add_field(name=member.name+" 参加禁止処分受ける", value="/banme によってbanされました。", inline=False)
        await message.channel.send(embed=embed)
    # 管理者が「/kick @[キックしたい人]」と発言したらそいつがキックされる処理
    if message.content.startswith('/kick'):
        if len(message.content.split()) == 1:
            await message.channel.send(random.choice(aori_g)+'/kick の構文は```/kick @[キックしたい人]```です。')
            return
        await skick(message,message.guild,'権限者に /kick されてしまいました。','/kick によるkick')
    # 管理者が「/ban @[BANしたい人]」と発言したらそいつがBANされる処理
    if message.content.startswith('/ban') :
        if len(message.content.split()) == 1:
            await message.channel.send(random.choice(aori_g)+'/ban の構文は```/ban @[BANしたい人]```です。')
            return
        await sban(message,message.guild,'権限者に /ban されてしまいました。','/ban によるban')
    # 管理者が「/warnguard @[warnguardを付与したい人]」と発言したらそいつがwarnguardを付与される処理
    if message.content.startswith('/guard'):
        if len(message.content.split()) == 1:
            await message.channel.send(random.choice(aori_g)+'/guard の構文は```/guard @[warnguardを付与したい人]```です。')
            return
        if (message.author.guild_permissions.administrator) == False:
            await message.channel.send('権限を持ってから実行しましょう。')
            return
        member = message.mentions[0]
        guild = message.guild
        role = guild.get_role(872005759045619732)
        await member.add_roles(role)
        embed=discord.Embed(title="warnguard", color=0x666666)
        embed.add_field(name=member.name+" へ警告ガード付与！", value="権限者が /warnguard してくれました。1回だけwarnを無効化できます！", inline=False)
        await message.channel.send(embed=embed)
    # 管理者が「/warn @[warnしたい人]」と発言したらwarnされる処理
    if message.content.startswith('/warn'):
        if len(message.content.split()) == 1:
            await message.channel.send(random.choice(aori_g)+'/warn の構文は```/warn @[warnしたい人]```です。')
            return
        await warn(message,message.guild,'権限者に /warn されました。2回warnされるとkickされます。','権限者に /warn され、warn回数が2回に到達しました。')
    # 管理者が「/mute @[黙らせたい人]」と発言したらそいつがmuteされる処理
    if message.content.startswith('/mute'):
        if (message.author.guild_permissions.administrator) == False:
            await message.channel.send('権限を持ってから実行しましょう。')
            return
        if len(message.content.split()) == 1:
            await message.channel.send(random.choice(aori_g)+'/mute の構文は```/mute @[黙らせたい人]```です。')
            return
        member = message.mentions[0]
        guild = message.guild
        role = guild.get_role(872093509035913216)
        await member.add_roles(role)
        embed=discord.Embed(title="mute!", color=0xaa3333)
        embed.add_field(name=member.name+" ミュート処分", value="権限者に /mute されてしまいました。発言が不可能になります。", inline=False)
        await message.channel.send(embed=embed)
    # 管理者が「/unmute @[unmuteしたい人]」と発言したらそいつがunmuteされる処理
    if message.content.startswith('/unmute'):
        if (message.author.guild_permissions.administrator) == False:
            await message.channel.send('権限を持ってから実行しましょう。')
            return
        if len(message.content.split()) == 1:
            await message.channel.send(random.choice(aori_g)+'/unmute の構文は```/unmute @[黙らせたい人]```です。')
            return
        member = message.mentions[0]
        guild = message.guild
        role = guild.get_role(872093509035913216)
        await member.remove_roles(role)
        embed=discord.Embed(title="unmute!", color=0x3333aa)
        embed.add_field(name=member.name+" ミュート解除", value="権限者が /unmute してくれました。発言が可能になります。", inline=False)
        await message.channel.send(embed=embed)
    # 管理者が「/unwarn @[warnしたい人]」と発言したらwarnが取り消される処理
    if message.content.startswith('/unwarn'):
        if (message.author.guild_permissions.administrator) == False:
            await message.channel.send('権限を持ってから実行しましょう。')
            return
        if len(message.content.split()) == 1:
            await message.channel.send(random.choice(aori_g)+'/unwarn の構文は```/unwarn @[unwarnしたい人]```です。')
            return
        if (message.author.guild_permissions.administrator) == False:
            return
        if len((message.mentions[0].roles)) <= 1:
            return
        if (message.mentions[0].roles)[1].id == 871975827758252042:
            member = message.mentions[0]
            guild = message.guild
            role = guild.get_role(871975827758252042)
            await member.remove_roles(role)
            embed=discord.Embed(title="unwarn!", color=0x6666ff)
            embed.add_field(name=member.name+" の警告取り消し", value="権限者が /unwarn してくれました。warn履歴を0回へリセットしました。", inline=False)
            await message.channel.send(embed=embed)
    # 「/search @[調べたい人]」と発言したらその人の情報を取得、表示する処理
    if message.content.startswith('/search'):
        if len(message.content.split()) == 1:
            await message.channel.send(random.choice(aori_g)+'/search の構文は```/search @[調べたい人]```です。')
            return
        if message.mention_everyone == True:
            embed=discord.Embed(title="search 結果", color=0xff6666)
            embed.add_field(name="みんな", value="みんなについて話すことはできません。一人だけを指定してください。", inline=False)
            await message.channel.send(embed=embed)
            return
        elif len(message.mentions) == 0:
            embed=discord.Embed(title="search 結果", color=0xff6666)
            embed.add_field(name="エラー", value="プレイヤーメンションで、一人だけを指定してください。", inline=False)
            await message.channel.send(embed=embed)
            return
        member = message.mentions[0]
        embed=discord.Embed(title="search 結果", color=0x666666)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name=member.name, value="この人について、話していきます。", inline=False)
        embed.add_field(name="いつからこのアカウントがあるか", value=member.created_at, inline=False)
        embed.add_field(name="いつからこのサーバーにいるか", value=member.joined_at, inline=False)
        embed.add_field(name="名前", value=member.name, inline=True)
        embed.add_field(name="ニックネーム", value=member.nick if (member.nick != None) else '無し', inline=True)
        embed.add_field(name="権限者であるか", value='YES' if (member.guild_permissions.administrator) else 'NO', inline=False)
        await message.channel.send(embed=embed)
    # 「/clear」と発言したらチャンネル内のログを消去する処理
    if message.content == '/clear':
        if message.author.guild_permissions.administrator:
            await message.channel.send('本当にチャンネル内のログを消去しますか？消去する場合は、この文にリアクションをつけてください。')
    # 管理者以外が「@everyone」と発言したらwarnされる処理
    if message.content.startswith('@everyone'):
        member = message.author
        guild = message.guild
        if len((member.roles)) >= 2:
            # すでにwarnされていたらkick
            for i in range(len(member.roles)):
                if member.roles[i].id == 871975827758252042:
                    await member.kick(reason="/warn によるwarn2回目")
                    embed=discord.Embed(title="kick!", color=0xff6666)
                    embed.add_field(name=member.name+" キックされる", value='権限者以外の everyone メンションによりwarn回数が2回に到達しました。', inline=False)
                    await message.channel.send(embed=embed)
                    return
                # warnguardの処理
                elif member.roles[i].id == 872005759045619732:
                    role = guild.get_role(872005759045619732)
                    await member.remove_roles(role)
                    embed=discord.Embed(title="warnguard!", color=0xff66ff)
                    embed.add_field(name=member.name+" が警告ガード！", value="warnが無効化されました！しかし、 "+member.name+" のwarnguardは壊れてしまいました・・・", inline=False)
                    await message.channel.send(embed=embed)
                    return
        role = guild.get_role(871975827758252042)
        await member.add_roles(role)
        embed=discord.Embed(title="warn!", color=0xffff66)
        embed.add_field(name=member.name+" へ警告", value='権限者以外の everyone メンションは禁止されています。2回warnされるとkickされます。', inline=False)
        await message.channel.send(embed=embed)
# await member.kick(reason="管理者以外の @everyone")

@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.content == '本当にチャンネル内のログを消去しますか？消去する場合は、この文にリアクションをつけてください。':
        if reaction.message.author.bot:
            if user.guild_permissions.administrator:
                await reaction.message.channel.send('それでは、消去を開始します。')
                await reaction.message.channel.purge()


bot.run(token)

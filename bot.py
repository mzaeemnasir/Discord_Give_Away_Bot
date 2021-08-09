import discord
from discord import member, user, embeds, channel
from discord.audit_logs import _transform_verification_level
from discord.ext import commands
import asyncio
import datetime
from discord.ext.commands.converter import clean_content
from discord.ext.commands.core import guild_only
import os

file_path = "//home//runner//GiveawayBotpy2//giveaway.gif"

from Token import TOKEN

intents = discord.Intents.default()
intents.all()

client = commands.Bot(intents=intents, command_prefix="-")


@client.event
async def on_ready():
    print("BOT is Ready....")


@client.command()
@commands.has_role("HITMAN")
async def giveaway(ctx, User: discord.Member, _time, *, link):
    if link == "https://upgrade.chat/cheggunloxx":
        channel_id = 831351625800089631
    else:
        channel_id = 867759773306454086

    role = discord.utils.get(ctx.guild.roles, name="chegg-members")
    await User.add_roles(role)
    print(f"Role Added {User.name}")
    await ctx.send("Done.")
    embeded = discord.Embed(
        title="🎉 Congratulations 🎉",
        description=f"""
    {User.mention} You have won Chegg - Premium Access For {int(_time)/3600} h  """,
        timestamp=datetime.datetime.utcnow(),
    )
    await User.send(file=discord.File(file_path))
    await User.send(embed=embeded)
    await client.get_channel(channel_id).send(file=discord.File(file_path))
    await client.get_channel(channel_id).send(embed=embeded)
    await asyncio.sleep(int(_time))
    await User.remove_roles(role)
    print(f"Role Removed {User.name}")
    await ctx.send(f"{User.name} Role Removed")
    end_emb = discord.Embed(
        title="🎉 Dear User🎉",
        description=f"""
    {User.mention} Your GiveAway time is Ended Please Upgrade Your Self.  BuyPremium  ->   {link} """,
        timestamp=datetime.datetime.utcnow(),
    )
    await User.send(embed=end_emb)
    await ctx.send(f"{User.name} GiveAway Time has Ended....")


client.run(TOKEN)

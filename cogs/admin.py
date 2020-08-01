#imports
import discord
import os
import asyncio
import typing
import colorama
from discord.ext import commands
from colorama import Fore, Style

#initialisation
colorama.init()

#create cog
class admin(commands.Cog):
    def __init__(self, client):
        self.client = client

	@commands.command(aliases = ['clear', 'c'])
    @commands.has_permissions(manage_messages = True)
    async def __clear(self, ctx, member: typing.Optional[discord.Member], amount : int):
        await ctx.message.delete()

        if member == None:
            await ctx.channel.purge(limit = amount)
        elif member != None and member in ctx.guild.members:
            number = 0
            def predicate(message):
                return message.author == member
            async for elem in ctx.channel.history().filter(predicate):
                await elem.delete()
                number += 1
                if number >= amount:
                    break

  	#kick 		
	@commands.command(aliases = ['kick'])
    @commands.has_permissions(kick_members = True)
    async def __ban(self, ctx, member: discord.Member, *, reason = None):
        await ctx.message.delete()

        if member is None:
            await ctx.send('�� �� ������� ������������, ������� ������ ��������!')
        else:
            if member.id == ctx.author.id:
                return await stx.send('������ - �� �����!')
            if member.id == ctx.guild.owner.id:
                return await ctx.send('� �� ��������� ������ ��������� ���� �������!')
            if ctx.author.top_role.position < member.top_role.position:
                return await ctx.send('�� ��� ������� ����! ������� ����� � ����������� �����.')
            guild_msg=discord.Embed(
            	description=f"{ctx.author.mention} ������� ��������� {member.mention} �� �������: `{reason}`"
            )
            dm_msg=discord.Embed(
            	description=f"�� ���� �������� �� ������� {ctx.guild.name}, ����������� {ctx.author.mention}, �� �������: `{reason}`"
            )
            if reason is None:
                reason="�� �������"
            await member.kick(member, reason=reason)
            await ctx.send(embed=guild_msg)
            await member.send(embed=dm_msg)
                    
                    
    #ban                		
	@commands.command(aliases = ['ban'])
    @commands.has_permissions(ban_members = True)
    async def __ban(self, ctx, member: discord.Member, *, reason = None):
        await ctx.message.delete()

        if member is None:
            await ctx.send('�� �� ������� ������������, ������� ������ ��������!')
        else:
            if member.id == ctx.author.id:
                return await stx.send('������ - �� �����!')
            if member.id == ctx.guild.owner.id:
                return await ctx.send('� �� ��������� ������ ��������� ���� �������!')
            if ctx.author.top_role.position < member.top_role.position:
                return await ctx.send('�� ��� ������� ����! ������� ����� � ����������� �����.')
            guild_msg=discord.Embed(
            	description=f"{ctx.author.mention} ������� ��������� {member.mention} �� �������: `{reason}`"
            )
            dm_msg=discord.Embed(
            	description=f"�� ���� �������� �� ������� {ctx.guild.name}, ����������� {ctx.author.mention}, �� �������: `{reason}`"
            )
            if reason is None:
                reason="�� �������"
            await member.ban(member, reason=reason)
            await ctx.send(embed=guild_msg)
            await member.send(embed=dm_msg)

#setup
def setup(client):
    client.add_cog(status(client))

        
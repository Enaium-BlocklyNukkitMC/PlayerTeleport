#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Project: PlayerTeleport
-----------------------------------------------------------
Copyright © 2020 | Enaium | All rights reserved.
"""
import cn.nukkit.Server as nk

tpalist = set()

manager.createCommand("tpa", u"传送到玩家", "tpa")


def tpa(sender, args):
    alllist = server.getInstance().getOnlinePlayers().values().toArray()

    for element in alllist:
        if element.getName().lower().__eq__(args[0].lower()):
            tpalist.add(TPA(sender, args[0].lower()))
            server.getPlayer(args[0]).sendTip(u"玩家" + sender.getName() + u"想传送到你!")
            return
    sender.sendTip(u"玩家" + args[0] + "不在线!")


manager.createCommand("tpaccept", u"接受传送", "tpaccept")


def tpaccept(sender, args):
    alllist = server.getInstance().getOnlinePlayers().values().toArray()

    for tpaElement in tpalist:
        if sender.getName().lower().__eq__(tpaElement.play2.lower()):
            for allElement in alllist:
                if allElement.getName().lower().__eq__(tpaElement.play1.getName().lower()):
                    allElement.teleport(sender)
                    tpalist.remove(tpaElement)
                    sender.sendTip(u"传送成功")
                    return
    sender.sendTip(u"没有传送!")


class TPA:
    def __init__(self, play1, play2):
        self.play1 = play1
        self.play2 = play2
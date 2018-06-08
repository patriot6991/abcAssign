import maya.cmds as mc


class WorldTransExport(object):
    def __init__(self):
        self.trans = []


    def export(self, *args):
        mc.polyCube()
        hoge = ''

a = WorldTransExport()
a.export()
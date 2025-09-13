
from dv_flow.mgr import ExtRgy as DfmExtRgy

class ExtRgy(DfmExtRgy):

    def __init__(self):
        self.ext_rgy = DfmExtRgy.inst()
        self.pkg_m = {}

    def addPackage(self, name, pkgfile):
        self.pkg_m[name] = pkgfile

    def hasPackage(self, name, search_path=True):
        if name in self.pkg_m.keys():
            return True
        else:
            return self.ext_rgy.hasPackage(name, search_path)
        
    def findPackagePath(self, name):
        if name in self.pkg_m.keys():
            return self.pkg_m[name]
        else:
            ret = self.ext_rgy.findPackagePath(name)
            return ret


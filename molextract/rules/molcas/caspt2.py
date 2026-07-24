from molextract.rule import Rule
from molextract.rules.abstract import SingleLineRule
from molextract.rules.molcas import log


class CASPT2XmsEnergy(Rule):

    START_TAG = r"       Total XMS-CASPT2 energies:"#"::    XMS-CASPT2 Root"
    END_TAG = r"       Eigenvectors:"

    def __init__(self):
        super().__init__(self.START_TAG, self.END_TAG)
        self.state = []

    def process(self, line):
        for lines in self:
            line = lines.split()
        self.state.append(float(line.split()[6]))
    
    def reset(self):
        tmp = self.state.copy()
        self.state.clear()
        self.__init__()
        return tmp



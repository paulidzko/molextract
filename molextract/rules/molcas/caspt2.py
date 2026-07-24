from molextract.rule import Rule
from molextract.rules.abstract import SingleLineRule
from molextract.rules.molcas import log


class CASPT2XmsEnergy(Rule):

    START_TAG = r"       Total XMS-CASPT2 energies:"#"::    XMS-CASPT2 Root"
    END_TAG = r"       Eigenvectors:"

    def __init__(self):
        super().__init__(self.START_TAG, self.END_TAG)
        if not hasattr(self, "state"): # in super():
            print("caspt2 initialized")
            self.state = []

    def process_lines(self, start_line):
        energies = []
        for lines in self:
            line = lines.strip()
            if line[:21] == "::    XMS-CASPT2 Root":
                energies.append(float(line.split()[6]))
        self.state.append(energies)
    
    def reset(self):
        tmp = self.state.copy()
        self.state.clear()
        return tmp



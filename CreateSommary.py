
class Sommary():
    def __init__(self,file):
        self.file = file
        self.createSommary()

    def getStringFile(self,fileName):
        file = open(fileName,"r")
        ch = file.read()
        file.close()
        return ch

    def selectClass(self,ch):
        res = ""
        cpt = 0
        ch = ch.split("\n")
        for k in range(len(ch)):
            cpt += 1
            if "class" in ch[k] and "):" in ch[k]:
                res += "line " + str(cpt) + "\n" + ch[k] + "\n"
                if '"""' in ch[k+2]:
                    res += ch[k+2] + "\n\n"
                else:
                    res += "\n\n"
        return res
                
    
    def createSommary(self):
        fileSommary = open("Sommary.txt","w")
        ch = self.selectClass(self.getStringFile(self.file))
        fileSommary.write(ch)
        fileSommary.close()

if __name__ == "__main__":
    s = Sommary("examples.py")

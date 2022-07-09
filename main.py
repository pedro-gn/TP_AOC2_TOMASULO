import re



instList = open("instrucoes.txt","r")
instList = instList.readlines()



"""
Recebe uma instrucao e retorna uma tupla contendo a oprecao e
os registradores.O segundo item da tupla sempre sera o registrador de destino (rd)
"""
def inst_decoder(inst) :
    op = inst[0:3].strip()
    regPattern = "R\d+"
    regList = re.findall(regPattern, inst)
    return (op,*regList)
     









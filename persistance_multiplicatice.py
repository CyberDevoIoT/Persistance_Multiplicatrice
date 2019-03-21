# -*- coding: utf-8 -*-

#==============================================================================#
# Name:                  $[ActiveDoc-Name]
# Purpose:
#------------------------------------------------------------------------------
# Author:      CyberDev
# Created:     Wed Feb  6 06:11:17 2019
# Copyright:   (c) CyberDev Wed Feb  6 06:11:17 2019
# Licence:     <your licence>                                                  
#==============================================================================#

#-------------------------------------------------#
#         Importation des modules externes        #
#-------------------------------------------------#



#-------------------------------------------------#
#            Définition des fonctions             #
#-------------------------------------------------#
def chercher(nb,liste):
	for i in range(0, len(liste)):
		if(i == nb):
			return False
		else:
			return True
		
		

def separateur():
	print("--------------------------------------------------------")



def compter(nb1,nb2):
	i = 0
	global iteration1
	global iteration2
	global iteration3
	global iteration4
	global iteration5
	global iteration6
	global iteration7
	global iteration8
	global iteration9
	global iteration10
	global iteration11
	global plus
	print("Demande de calculs entre " + str(nb1) + " et " + str(nb2))
	separateur()
	for i in range(nb1, nb2+1):
		result = 11
		itera = 0
		liste = list("".join(str(i).split()))
		while result>=10:
			for j in range(0,len(liste)):
				if(j==0):
					result = int(liste[j])
				else:
					result *= int(liste[j])
			itera += 1
			result = result
			liste = list("".join(str(result).split()))
		if(itera == 1):
			v_f = chercher(result,iteration1)
			if(v_f):
				iteration1.append(i)
		elif(itera == 2):
			iteration2.append(i)
		elif(itera == 3):
			iteration3.append(i)
		elif(itera == 4):
			iteration4.append(i)
		elif(itera == 5):
			iteration5.append(i)
		elif(itera == 6):
			iteration6.append(i)
		elif(itera == 7):
			iteration7.append(i)
		elif(itera == 8):
			iteration8.append(i)
		elif(itera == 9):
			iteration9.append(i)
		elif(itera == 10):
			iteration10.append(i)
		elif(itera == 11):
			iteration11.append(i)
		else:
			print("Aurions nous trouvé un nouveau de plus d'itérations ?")
			plus.append(i)


#-------------------------------------------------#
#              Programme principal                #
#-------------------------------------------------#
iteration1 = []
iteration2 = []
iteration3 = []
iteration4 = []
iteration5 = []
iteration6 = []
iteration7 = []
iteration8 = []
iteration9 = []
iteration10 = []
iteration11 = []
plus = []
nb_min = eval(input("Entre un nombre minimum : "))
nb_max = eval(input("Entre un nombre maximum : "))
separateur()
compter(nb_min, nb_max)
separateur()
print("Iterations 1 :")
print(iteration1)
separateur()
print("Iterations 2 :")
print(iteration2)
separateur()
print("Iterations 3 :")
print(iteration3)
separateur()
print("Iterations 4 :")
print(iteration4)
separateur()
print("Iterations 5 :")
print(iteration5)
separateur()
print("Iterations 6 :")
print(iteration6)
separateur()
print("Iterations 7 :")
print(iteration7)
separateur()
print("Iterations 8 :")
print(iteration8)
separateur()
print("Iterations 9 :")
print(iteration9)
separateur()
print("Iterations 10 :")
print(iteration10)
separateur()
print("Iterations 11 :")
print(iteration11)
separateur()
print("Plus...")
print(plus)

#----------fonction de test du module-------------#
#if __name__ == '__main__':
    #main()



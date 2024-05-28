""""
def factorielle(n):
   if n == 0:
       return 1
   else:
       return n * factorielle(n-1)

def arrangement(n,p):
   return factorielle(n)/factorielle(n-p)

tu peux mettre les trues a la place
a = int(input("entrez une année:"))
def bissextile(a):
    if a % 4 == 0:
        print("l'année est bissextile.")
        if a % 100 != 0:
            print("l'année est bissextile.")
        else:
            print("l'année n'est pas bissextile.")
    elif a % 400 == 0:
        print("l'année est bissextile.")
    else:
        print("l'année n'est pas bissextile.")
bissextile(a)

def signe(a, b):
    if a > 0 and b > 0 or a < 0 and b < 0:
        print("a et b sont de meme signe")
    else:
        print("a et b ne sont pas de meme signe")

a = int(input("Veuillez entrez une valeur pour a:"))
b = int(input("Veuillez entrez une valeur pour b:"))
signe(a, b)
signe(a, b)
def maximun(a, b):
    m = 0
    if a > b:
        return a
    else:
        return b

c = maximun(a, b)
print("la maximun entre a et b est:", c)

def minimun(a, b):
    m = 0
    if a < b:
        return a
    else:
        return b


a = int(input("Veuillez entrez une valeur pour a:"))
b = int(input("Veuillez entrez une valeur pour b:"))
print("le minimum entre a et b est:",minimun(a, b))


def ouverture(h,j):
    i = 0
    while i < len(jour):
         if jour[i] == j:
             if jour[i] == jour[0]:
                  print("le",j,"le restaurant est fermer.")
                  return
             else:
                  print("le",j,"le restaurant est ouvert.")
                  break
         i += 1
    else:
        print("le jour saisie n'est pas un jour de la semaine")
        return

    if h in heure:
        print("le restaurant est ouvert.")
    elif j == jour[6] and h == heure[0:6]:
        print("mais à cette heure",h, "le restaurant est ouvert.")
    elif j == jour[0]:
        print("le restaurant est fermer.")
    else:
        print("le restaurant est fermer.")

heure = [7,8,9,10,11,12,13,16,17,18,19,20,21,22]
jour = ['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']
j = input("veuillez entrez un jour:")
h = int(input("veuillez entrez une heure:"))
ouverture(h,j)

def montant(p):

    if p < 20:
        print("le montant de l'affranchisement de la lettre est 280F.")
    elif p >= 20 and p < 50:
        print("le montant de l'affranchisement de la lettre est 440F ")
    elif p >= 50:
        print("le montant de l'affranchisement de la lettre est 670F ")


p = int(input("veuillez entrer le poids de la lettre:"))
montant(p)

def first(n):
    if n > 2:
        for i in range(2,n):
            if n % i == 0:
                print("non le nombre n'est pas premier ")
            else:
                print(" le nombre est premier")
            return
    elif n == 2:
        print("premier")
    else:
        print("non")
n = int(input("nombre:"))
first(n)
"""
revenu_impossable = int(input("veuillez entrez votre renenu:"))
nombre_part = int(input("Veuillez entrez le nombre de part:"))
def tax(revenu_impossable,nombre_part):
    revenu_fiscal = revenu_impossable/nombre_part
    if revenu_fiscal < 50000:
        impot_du = 0
    elif 50000<= revenu_fiscal <= 100000:
        impot_du = 0.10*(revenu_fiscal)
    elif 100000 <= revenu_fiscal <= 200000:
        impot_du = 0.25*(revenu_fiscal)
    elif revenu_fiscal > 200000:
        impot_du = 0.50 * (revenu_fiscal)
        return
    impot =  impot_du * nombre_part
    return impot

impot = tax(revenu_impossable, nombre_part)
print(impot)
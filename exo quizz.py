#liste des question et reponse
a_1  = ("quel symbole utilise-t-on pour écrire un commentaire en python ?", "//", "#", "--", 1)
a_2  = ("quelle fonction sert à afficher du texte à l’écran ?", "print()", "echo()", "affiche()", 0)
a_3  = ("comment déclare-t-on une liste en python ?", "{1,2,3}", "(1,2,3)", "[1,2,3]", 2)
a_4  = ("quelle méthode transforme une chaîne en majuscules ?", "upper()", "capitalize()", "majuscule()", 0)
a_5  = ("quelle est la valeur de len('python') ?", "5", "6", "7", 1)
a_6  = ("comment vérifier le type d’une variable ?", "typeof(x)", "type(x)", "class(x)", 1)
a_7  = ("comment définir une fonction en python ?", "function f():", "def f():", "func f():", 1)
a_8  = ("quel mot-clé crée une boucle qui parcourt une liste ?", "loop", "for", "foreach", 1)
a_9  = ("quelle méthode ajoute un élément à une liste ?", "push()", "insert()", "append()", 2)
a_10 = ("comment importer une bibliothèque externe ?", "require lib", "import lib", "include lib", 1)
a_11 = ("quelle est la sortie de print(3**2) ?", "6", "9", "8", 1)
a_12 = ("que fait input() ?", "donne un nombre aléatoire", "demande une saisie utilisateur", "affiche du texte", 1)
a_13 = ("comment écrire une condition 'si' ?", "if ... :", "si ... alors", "when ...", 0)
a_14 = ("quel mot-clé arrête une boucle prématurément ?", "exit", "stop", "break", 2)
a_15 = ("quel mot-clé sert à ignorer une itération dans une boucle ?", "skip", "continue", "next", 1)
a_16 = ("comment déclare-t-on un dictionnaire ?", "[clé:valeur]", "{clé:valeur}", "(clé=valeur)", 1)
a_17 = ("quelle est la sortie de bool('') ?", "true", "false", "none", 1)
a_18 = ("que retourne range(5) ?", "[1,2,3,4,5]", "[0,1,2,3,4]", "[0,1,2,3,4,5]", 1)
a_19 = ("comment ouvrir un fichier en lecture ?", "open('f.txt','w')", "open('f.txt','r')", "open('f.txt','rw')", 1)
a_20 = ("que fait int('5') ?", "erreur", "convertit '5' en entier", "convertit en flottant", 1)
a_21 = ("comment arrondir un nombre ?", "round()", "arrondi()", "approx()", 0)
a_22 = ("quel est le type de 3.14 ?", "int", "float", "double", 1)
a_23 = ("comment définir une classe ?", "class nom:", "define nom:", "objet nom:", 0)
a_24 = ("quel mot-clé sert à créer une boucle infinie ?", "loop", "while", "repeat", 1)
a_25 = ("que fait list('abc') ?", "['abc']", "['a','b','c']", "('a','b','c')", 1)


# création d'une liste avec les 50 questions
questionlist = [a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9, a_10, a_11, a_12, a_13, a_14, a_15, a_16, a_17, a_18, a_19, a_20, a_21, a_22, a_23, a_24, a_25]
#  programme principale
class Quizz:
    def __init__(self, questions, vies=3):
        self.questions = questions  # liste de questions (tuple)
        self.vies = vies  # nb de vies

    def poser_question(self, question_tuple):
        question, r1, r2, r3, bonne = question_tuple

        # afficher la question
        print("\n" + question)
        print("0:", r1)
        print("1:", r2)
        print("2:", r3)

        # demander la réponse
        try:
            choix = int(input("ta réponse (0-2) : "))
        except:
            print("entrée invalide, -1 vie")
            self.vies -= 1
            return

        # vérifier si correct
        if choix == bonne:
            print("bonne réponse !")
        else:
            self.vies -= 1
            print("mauvaise réponse il te reste", self.vies, "vie")

    def jouer(self):
        print("bienvenue dans le quizz python, tu as", self.vies, "vie")

        for q in self.questions:
            if self.vies <= 0:
                print("game over !")
                break
            self.poser_question(q)

        if self.vies > 0:
            print("\nbravo tu as terminé le quizz avec", self.vies, "vie restante !")
# lancement du programme principal
if __name__ == "__main__":
    # on crée l'objet quizz avec la liste de questions
    jeu = Quizz(questionlist, vies=3)
    # on démarre le jeu
    jeu.jouer()

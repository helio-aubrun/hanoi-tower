def hanoi(n, source, target, auxiliary):
    """
    Résout le problème de la Tour d'Hanoi avec n disques entre trois bâtonnets.
    
    Args:
    n (int): Nombre de disques.
    source (str): Bâtonnet source.
    target (str): Bâtonnet cible.
    auxiliary (str): Bâtonnet auxiliaire.
    """
    if n > 0:
        # Déplace n-1 disques de la source à l'auxiliaire, en passant par la cible
        hanoi(n-1, source, auxiliary, target)
        
        # Déplace le disque restant de la source à la cible
        print(f"{source} -> {target}")
        
        # Déplace les n-1 disques de l'auxiliaire à la cible, en passant par la source
        hanoi(n-1, auxiliary, target, source)

# Fonction principale pour lire l'entrée utilisateur et appeler la fonction hanoi
def main():
    # Lire l'entrée utilisateur
    input_str = input("Entrez le nombre de disques suivi du nombre de bâtonnets séparés par une virgule: ")
    disks, pegs = map(int, input_str.split(','))
    
    # Appeler la fonction hanoi avec les paramètres appropriés
    hanoi(disks, '1', '2', '3')

if __name__ == "__main__":
    main()
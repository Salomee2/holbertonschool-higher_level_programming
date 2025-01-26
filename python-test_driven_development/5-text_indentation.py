#!/usr/bin/python3
"""Text indentation function"""

def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: '.', '?', and ':'"""
    
    # Checking if the input is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Initialisation d'un texte temporaire pour accumuler les résultats
    temp_text = ""
    
    # On parcourt chaque caractère du texte
    for char in text:
        temp_text += char
        
        # Ajout d'un saut de ligne après '.', '?', ou ':'
        if char in ['.', '?', ':']:
            print(temp_text.strip())  # On affiche la ligne sans espace au début/fin
            temp_text = ""  # Réinitialise temp_text après un saut de ligne
            
    # Affichage du texte restant s'il existe
    if temp_text:
        print(temp_text.strip())

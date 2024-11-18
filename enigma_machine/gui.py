import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json
from enigma_machine import EnigmaMachine
from plugboard import Plugboard
from reflector import Reflector
from rotor import Rotor
from state import EnigmaState

enigma_state = EnigmaState()
def run_enigma_machine():
        def initialize_enigma():
            rotor_order = [rotor_var_1.get(), rotor_var_2.get(), rotor_var_3.get()]
            rotor_configs = {
                "Rotor I": Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch="Q", position=entry_positions[0].get().upper(), ring_setting=int(entry_rings[0].get())),
                "Rotor II": Rotor(wiring="AJDKSIRUXBLHWTMCQGZNPYFVOE", notch="E", position=entry_positions[1].get().upper(), ring_setting=int(entry_rings[1].get())),
                "Rotor III": Rotor(wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO", notch="V", position=entry_positions[2].get().upper(), ring_setting=int(entry_rings[2].get())),
                "Rotor IV": Rotor(wiring="ESOVPZJAYQUIRHXLNFTGKDCMWB", notch="J", position=entry_positions[0].get().upper(), ring_setting=int(entry_rings[0].get())),
                "Rotor V": Rotor(wiring="VZBRGITYUPSDNHLXAWMJQOFECK", notch="Z", position=entry_positions[1].get().upper(), ring_setting=int(entry_rings[1].get())),
            }

            rotors = [
                rotor_configs[rotor_order[0]],
                rotor_configs[rotor_order[1]],
                rotor_configs[rotor_order[2]]
            ]

            plugboard_pairs = entry_plugboard.get().split(", ")
            plugboard = Plugboard(plugboard_pairs)

            reflector = Reflector(entry_reflector.get())

            return EnigmaMachine(rotors, plugboard, reflector)



        def encrypt_message():
            try:
                # Initialiser la machine Enigma si nécessaire
                if enigma_state.machine is None:
                    enigma_state.machine = initialize_enigma()
                
                # Sauvegarder également l'état initial des rotors
                enigma_state.initial_config = {
                    "rotor_order": [rotor_var_1.get(), rotor_var_2.get(), rotor_var_3.get()],
                    "initial_positions": [entry_positions[0].get().upper(), entry_positions[1].get().upper(), entry_positions[2].get().upper()],
                    "ring_settings": [int(entry_rings[0].get()), int(entry_rings[1].get()), int(entry_rings[2].get())],
                    "plugboard": entry_plugboard.get(),
                    "reflector": entry_reflector.get()
                }

                # Chiffrer le message
                message = entry_message.get().upper()
                encrypted = enigma_state.machine.encrypt(message)

                # Sauvegarder le dernier message et le message chiffré dans l'état
                enigma_state.last_message = message
                enigma_state.last_encrypted_message = encrypted
                
                # Sauvegarder les positions finales des rotors après le chiffrement
                enigma_state.final_positions = [rotor.position for rotor in enigma_state.machine.rotors]



                # Afficher le message chiffré à l'utilisateur
                messagebox.showinfo("Encrypted Message", f"Encrypted Message: {encrypted}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to encrypt message: {str(e)}")






        def decrypt_message():
            try:
                # Initialiser la machine Enigma si nécessaire
                if enigma_state.machine is None:
                    enigma_state.machine = initialize_enigma()
                else:
                    enigma_state.machine.reset_rotors()

                # Déchiffrer le message
                message = entry_message.get().upper()
                decrypted = enigma_state.machine.encrypt(message)

                messagebox.showinfo("Decrypted Message", f"Decrypted Message: {decrypted}")
            except ValueError as e:
                messagebox.showerror("Configuration Error", str(e))


        def reset_machine():
            try:
                enigma_state.machine = initialize_enigma()
                messagebox.showinfo("Info", "Enigma machine reset to initial state.")
            except ValueError as e:
                messagebox.showerror("Configuration Error", str(e))



        def save_configuration():
            try:
                # Charger les configurations existantes (s'il y en a)
                try:
                    with open("enigma_encrypted_message.json", "r") as f:
                        configurations = json.load(f)
                        # Vérifier que le format est une liste
                        if not isinstance(configurations, list):
                            configurations = []
                except (FileNotFoundError, json.JSONDecodeError):
                    configurations = []

                # Créer une nouvelle configuration à partir des entrées de l'utilisateur
                
                config = {
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "rotor_order(gauche a droite)": enigma_state.initial_config["rotor_order"],
                    "initial_positions": enigma_state.initial_config["initial_positions"],
                    "ring_settings": enigma_state.initial_config["ring_settings"],
                    "plugboard": enigma_state.initial_config["plugboard"],
                    "reflector": enigma_state.initial_config["reflector"],
                }
                
                # Ajouter les positions réelles des rotors après le chiffrement
                if enigma_state.final_positions:
                    config["final_positions"] = enigma_state.final_positions

                # Si un message a été chiffré, l'ajouter à la configuration
                if enigma_state.last_message and enigma_state.last_encrypted_message:
                    config["message"] = enigma_state.last_message
                    config["encrypted_message"] = enigma_state.last_encrypted_message

                # Ajouter la nouvelle configuration aux configurations existantes
                configurations.append(config)

                # Sauvegarder toutes les configurations
                with open("enigma_encrypted_message.json", "w") as f:
                    json.dump(configurations, f, indent=4)

                messagebox.showinfo("Info", "Configuration saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save configuration: {str(e)}")






        root = tk.Tk()
        root.title("Enigma Machine Configuration")
        root.configure(bg="#2F4F4F")
        root.geometry("1400x800")

        title_label = tk.Label(root, text="Enigma Machine Simulator", font=("Arial", 16, "bold"), bg="#2F4F4F", fg="white")
        title_label.grid(row=0, column=0, columnspan=10, pady=10)

        # Reflector Configuration
        tk.Label(root, text="Reflector:", bg="#2F4F4F", fg="white", font=("Arial", 12, "bold")).grid(row=1, column=0, pady=20, sticky="w")
        tk.Label(root, text="Wiring:", bg="#2F4F4F", fg="white").grid(row=2, column=0, sticky="w")
        entry_reflector = tk.Entry(root, width=32)
        entry_reflector.insert(0, "YRUHQSLDPXNGOKMIEBFZCWVJAT")
        entry_reflector.grid(row=2, column=1, padx=20)

        # Rotor Order Selection
        tk.Label(root, text="Rotor Order", bg="#2F4F4F", fg="white", font=("Arial", 12, "bold")).grid(row=4, column=0, pady=20)
        rotor_var_1 = tk.StringVar(value="Rotor I")
        rotor_var_2 = tk.StringVar(value="Rotor II")
        rotor_var_3 = tk.StringVar(value="Rotor III")

        tk.OptionMenu(root, rotor_var_1, "Rotor I", "Rotor II", "Rotor III", "Rotor IV", "Rotor V").grid(row=4, column=1, padx=20)
        tk.OptionMenu(root, rotor_var_2, "Rotor I", "Rotor II", "Rotor III", "Rotor IV", "Rotor V").grid(row=4, column=2, padx=20)
        tk.OptionMenu(root, rotor_var_3, "Rotor I", "Rotor II", "Rotor III", "Rotor IV", "Rotor V").grid(row=4, column=5, padx=20)

        # Rotor Configurations
        entry_positions = []
        entry_rings = []
        entries = [("Rotor A", 0), ("Rotor B", 2), ("Rotor C", 5)]

        for i, (label, col) in enumerate(entries):
            tk.Label(root, text=label, bg="#2F4F4F", fg="white", font=("Arial", 12, "bold")).grid(row=5, column=col, pady=20)


            tk.Label(root, text="Initial Position:", bg="#2F4F4F", fg="white").grid(row=7, column=col, sticky="w")
            entry_position = tk.Entry(root, width=5)
            entry_position.insert(0, "A")
            entry_position.grid(row=7, column=col + 1, padx=10)
            entry_positions.append(entry_position)

            tk.Label(root, text="Ring Setting:", bg="#2F4F4F", fg="white").grid(row=8, column=col, sticky="w")
            entry_ring = tk.Entry(root, width=5)
            entry_ring.insert(0, "0")
            entry_ring.grid(row=8, column=col + 1, padx=10)
            entry_rings.append(entry_ring)

        # Plugboard Configuration
        tk.Label(root, text="Plugboard Pairs (e.g., AB, CD, EF):", bg="#2F4F4F", fg="white").grid(row=15, column=0, sticky="w", columnspan=2, pady=20)
        entry_plugboard = tk.Entry(root, width=30)
        entry_plugboard.insert(0, "AB, CD, EF")
        entry_plugboard.grid(row=15, column=2, columnspan=1, padx=5)

        # Message to Encrypt/Decrypt
        tk.Label(root, text="Message:", bg="#2F4F4F", fg="white").grid(row=17, column=0, sticky="w", columnspan=2, pady=20)
        entry_message = tk.Entry(root, width=30)
        entry_message.grid(row=17, column=2, columnspan=1, padx=5)

        # Buttons
        tk.Button(root, text="Encrypt Message", command=encrypt_message, bg="#4682B4", fg="white", font=("Arial", 12)).grid(row=35, column=1, columnspan=2, pady=20)
        tk.Button(root, text="Decrypt Message", command=decrypt_message, bg="#5F9EA0", fg="white", font=("Arial", 12)).grid(row=36, column=1, columnspan=2, pady=20)
        tk.Button(root, text="Save Configuration", command=save_configuration, bg="#8B4513", fg="white", font=("Arial", 12)).grid(row=35, column=3, columnspan=2, pady=20)
        tk.Button(root, text="Reset Machine", command=reset_machine, bg="#556B2F", fg="white", font=("Arial", 12)).grid(row=36, column=3, columnspan=2, pady=20)

        root.mainloop()



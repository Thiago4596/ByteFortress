import os
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Gerar par de chaves RSA
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Salvar chave privada
    with open("private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    # Salvar chave pública
    with open("public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    messagebox.showinfo("Sucesso", "Chaves RSA geradas e salvas.")
    return private_key, public_key

# Função para criptografar o arquivo
def encrypt_file(file_path, public_key):
    aes_key = os.urandom(32)
    iv = os.urandom(16)
    
    encrypted_aes_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(file_path, "rb") as f:
        file_data = f.read()
    
    encrypted_data = encryptor.update(file_data) + encryptor.finalize()

    with open(f"{file_path}.encrypted", "wb") as f:
        f.write(encrypted_aes_key + iv + encrypted_data)

    messagebox.showinfo("Sucesso", f"Arquivo '{file_path}' criptografado com sucesso.")

# Função para descriptografar o arquivo
def decrypt_file(encrypted_file_path, private_key):
    with open(encrypted_file_path, "rb") as f:
        encrypted_data = f.read()

    encrypted_aes_key = encrypted_data[:256]
    iv = encrypted_data[256:272]
    encrypted_file_content = encrypted_data[272:]

    aes_key = private_key.decrypt(
        encrypted_aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_file_content) + decryptor.finalize()

    decrypted_file_path = encrypted_file_path.replace(".encrypted", ".decrypted")
    with open(decrypted_file_path, "wb") as f:
        f.write(decrypted_data)

    messagebox.showinfo("Sucesso", f"Arquivo descriptografado com sucesso: '{decrypted_file_path}'")

# Funções para Interface Gráfica
def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def perform_encryption():
    file_path = file_entry.get()
    if not file_path:
        messagebox.showwarning("Aviso", "Selecione um arquivo.")
        return

    try:
        _, public_key = load_keys()
        encrypt_file(file_path, public_key)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao criptografar o arquivo: {e}")

def perform_decryption():
    file_path = file_entry.get()
    if not file_path:
        messagebox.showwarning("Aviso", "Selecione um arquivo.")
        return

    try:
        private_key, _ = load_keys()
        decrypt_file(file_path, private_key)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao descriptografar o arquivo: {e}")

def load_keys():
    try:
        with open("private_key.pem", "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
                backend=default_backend()
            )
        with open("public_key.pem", "rb") as f:
            public_key = serialization.load_pem_public_key(
                f.read(),
                backend=default_backend()
            )
        return private_key, public_key
    except FileNotFoundError:
        messagebox.showinfo("Info", "Chaves RSA não encontradas. Gerando novas chaves.")
        return generate_rsa_keys()

# Configuração da Interface Gráfica
root = tk.Tk()
root.title("Criptografia de Arquivo Assimétrica")
root.geometry("400x200")

# Campo de seleção de arquivo
file_label = tk.Label(root, text="Arquivo:")
file_label.pack(pady=5)

file_entry = tk.Entry(root, width=50)
file_entry.pack(pady=5)

select_button = tk.Button(root, text="Selecionar Arquivo", command=select_file)
select_button.pack(pady=5)

# Botões de Criptografar e Descriptografar
encrypt_button = tk.Button(root, text="Criptografar", command=perform_encryption)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(root, text="Descriptografar", command=perform_decryption)
decrypt_button.pack(pady=5)

root.mainloop()

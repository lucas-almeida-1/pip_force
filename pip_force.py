import subprocess
import time

def install_package(package_name):
    """
    Tenta instalar um pacote Python usando pip, repetindo em caso de falha.
    """
    while True:
        try:
            print(f"Tentando instalar {package_name}...")
            subprocess.check_call(["pip", "install", package_name])
            print(f"{package_name} instalado com sucesso!")
            break  # Sai do loop se a instalação for bem-sucedida
        except subprocess.CalledProcessError as e:
            print(f"Erro ao instalar {package_name}: {e}")
            print("Tentando novamente em 5 segundos...")
            time.sleep(5)
        except FileNotFoundError as e:
            print(f"Erro: pip não encontrado. Verifique se o Python e o pip estão instalados e configurados corretamente.")
            break

if __name__ == "__main__":
    package_to_install = input("Digite o nome do pacote a ser instalado: ")
    install_package(package_to_install)
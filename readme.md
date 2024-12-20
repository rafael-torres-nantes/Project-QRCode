# Gerador de QR Codes Personalizados

## 👨‍💻 Projeto desenvolvido por:
[Rafael Torres Nantes](https://github.com/rafael-torres-nates)

## Índice

* 📚 Contextualização do projeto
* 🛠️ Tecnologias/Ferramentas utilizadas
* 🖥️ Funcionamento do sistema
   * 🧩 Parte 1 - Geração de QR Codes
* 📁 Estrutura do projeto
* 📌 Como executar o projeto
* 🕵️ Dificuldades Encontradas

## 📚 Contextualização do projeto

O projeto tem como objetivo criar uma solução automatizada para gerar **QR Codes personalizados** utilizando a biblioteca **qrcode** em Python. O sistema permite a criação de QR Codes básicos, com logotipos centralizados, com imagens de fundo personalizadas e a partir de dados de imagens.

## 🛠️ Tecnologias/Ferramentas utilizadas

[<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">](https://www.python.org/)
[<img src="https://img.shields.io/badge/qrcode-3776AB?logo=python&logoColor=white">](https://pypi.org/project/qrcode/)
[<img src="https://img.shields.io/badge/Pillow-3776AB?logo=python&logoColor=white">](https://python-pillow.org/)
[<img src="https://img.shields.io/badge/Visual_Studio_Code-007ACC?logo=visual-studio-code&logoColor=white">](https://code.visualstudio.com/)

## 🖥️ Funcionamento do sistema

### 🧩 Parte 1 - Geração de QR Codes

O sistema foi desenvolvido utilizando **Python** e a biblioteca **qrcode**. As principais funcionalidades incluem a geração de QR Codes básicos, com logotipos centralizados, com imagens de fundo personalizadas e a partir de dados de imagens.

* **QRCodeGenerator**: A classe 

QRCodeGenerator em qr_code.py contém métodos para gerar diferentes tipos de QR Codes.
   * **generate_qr_code**: Gera um QR Code básico e salva como imagem PNG.
   * **generate_qr_code_with_logo**: Gera um QR Code com um logotipo centralizado.
   * **generate_qr_code_with_background**: Gera um QR Code com uma imagem de fundo personalizada.
   * **generate_qr_code_from_image**: Gera um QR Code a partir dos dados de uma imagem.

## 📁 Estrutura do projeto

A estrutura do projeto é organizada da seguinte maneira:

```
.
├── images/
├── logo/
├── qrcode_images/
├── qrcode_links/
├── qr_code.py
├── .gitignore
├── readme.md
└── requirements.txt
```

## 📌 Como executar o projeto

Para executar o projeto localmente, siga as instruções abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o script:**
   ```bash
   python qr_code.py
   ```

## 🕵️ Dificuldades Encontradas

Durante o desenvolvimento do projeto, algumas dificuldades foram enfrentadas, como:

- **Integração de logotipos e fundos personalizados:** Ajustar o tamanho e a posição dos logotipos e imagens de fundo para garantir que o QR Code permaneça legível.
- **Manutenção da qualidade da imagem:** Garantir que a qualidade da imagem do QR Code não seja comprometida ao adicionar elementos personalizados.
- **Gerenciamento de diretórios:** Verificar e criar diretórios automaticamente para salvar os QR Codes gerados.
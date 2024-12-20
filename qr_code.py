import os
import qrcode  # Biblioteca para geração de QR Codes
from PIL import Image  # Biblioteca para manipulação de imagens
from qrcode.image.styledpil import StyledPilImage  # Para adicionar estilos ao QR Code
from qrcode.image.styles.colormasks import ImageColorMask  # Para aplicar máscaras de cores
import base64  # Para codificar e decodificar imagens em base64
import io  # Para manipular fluxos de dados em memória


class QRCodeGenerator:
    """
    Classe responsável por gerar QR Codes com suporte a personalizações como logos e fundos.
    """

    def __init__(self, url):
        """
        Inicializa o gerador com um URL que será embutido no QR Code.

        :param url: O link ou dado que será codificado no QR Code.
        """
        self.url = url

    @staticmethod
    def _ensure_directory_exists(path):
        """
        Verifica e cria o diretório do caminho especificado, se não existir.

        :param path: Caminho do arquivo.
        """
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

    def generate_qr_code(self, output_path):
        """
        Gera um QR Code básico e salva como imagem PNG.

        :param output_path: Caminho do arquivo para salvar o QR Code gerado.
        """
        output_path = os.path.join("qrcode_links/", output_path)
        self._ensure_directory_exists(output_path)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.url)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save(output_path)

        print(f"QR Code gerado e salvo como '{output_path}'.")

    def generate_qr_code_with_logo(self, output_path, logo_path):
        """
        Gera um QR Code com um logotipo centralizado.

        :param output_path: Caminho do arquivo para salvar o QR Code gerado.
        :param logo_path: Caminho para o arquivo de imagem do logotipo.
        """
        output_path = os.path.join("qrcode_links/", output_path)
        self._ensure_directory_exists(output_path)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=2,
        )
        qr.add_data(self.url)
        qr.make(fit=True)

        qr_img = qr.make_image(fill='black', back_color='white')
        logo = Image.open(logo_path).resize((75, 75), Image.LANCZOS)
        offset = ((qr_img.size[0] - 75) // 2, (qr_img.size[1] - 75) // 2)
        qr_img.paste(logo, offset, mask=logo.split()[3] if logo.mode == 'RGBA' else None)
        qr_img.save(output_path)

        print(f"QR Code com logotipo gerado e salvo como '{output_path}'.")

    def generate_qr_code_with_background(self, output_path, background_path):
        """
        Gera um QR Code com uma imagem de fundo personalizada.

        :param output_path: Caminho do arquivo para salvar o QR Code gerado.
        :param background_path: Caminho para o arquivo de imagem de fundo.
        """
        output_path = os.path.join("qrcode_links/", output_path)
        self._ensure_directory_exists(output_path)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=2,
        )
        qr.add_data(self.url)
        qr.make(fit=True)

        background_img = Image.open(background_path)
        qr_img = qr.make_image(
            image_factory=StyledPilImage,
            color_mask=ImageColorMask(
                back_color=(255, 255, 255), color_mask_image=background_img
            )
        )
        qr_img.save(output_path)

        print(f"QR Code com fundo personalizado gerado e salvo como '{output_path}'.")

    def generate_qr_code_from_image(self, image_path, output_path):
        """
        Gera um QR Code a partir dos dados de uma imagem.

        :param image_path: Caminho para a imagem cujos dados serão embutidos no QR Code.
        :param output_path: Caminho do arquivo para salvar o QR Code gerado.
        """
        output_path = os.path.join("qrcode_images/", output_path)
        self._ensure_directory_exists(output_path)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(image_path)
        qr.make(fit=True)

        img = qr.make_image(fill_color='white', back_color='#282d39').convert("RGBA")
        background = Image.new("RGBA", img.size)
        qr_code = Image.alpha_composite(background, img)

        memory = io.BytesIO()
        qr_code.save(memory, format="PNG")
        memory.seek(0)

        base64_img = "data:image/png;base64," + base64.b64encode(memory.getvalue()).decode('ascii')
        qr_code.save(output_path)

        print(f"QR Code gerado a partir da imagem e salvo como '{output_path}'.")
        return base64_img


# Exemplo de uso
if __name__ == "__main__":
    url = "https://www.google.com"
    qr_generator = QRCodeGenerator(url)

    qr_generator.generate_qr_code("qrcode.png")
    logo_path = "./logo/youtube_logo.png"
    qr_generator.generate_qr_code_with_logo("qrcode_with_logo.png", logo_path)

    background_path = "./images/Cigarrinho.jpeg"
    qr_generator.generate_qr_code_with_background("qrcode_with_background.png", background_path)

    image_path = "./images/Cigarrinho.jpeg"
    qr_generator.generate_qr_code_from_image(image_path, "qrcode_from_image.png")

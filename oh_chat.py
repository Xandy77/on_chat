# biblioteca
import flet as ft
from dataclasses import dataclass

@dataclass
class Mensagem:
    usuario: str
    texto:str
    tipo_msg: str

    def __del__(self):
        return f"{self.usuario} destruído com sucesso"

def main(page: ft.Page): # envia mensagem
    page.title = "Oh Chat!"
    page.theme_mode = ft.ThemeMode.LIGHT

    def on_message(msg: Mensagem):
        if msg.tipo_msg == "chat_message": # identifica o usuario
            chat.controls.append(ft.Text(f"{msg.usuario}: {msg.texto}"))
        elif msg.tipo_msg == "login_message":
            chat.controls.append(ft.Text(msg.texto, italic=True, color=ft.colors.BLACK45, size=12))
        else:
            ...
        page.update()

    page.pubsub.subscribe(on_message) # permite a troca de mensagens

    def enviar(e): # aqui recebe a mensagem
        page.pubsub.send_all(Mensagem(usuario=page.session.get('nome_usuario'), texto=nova_msg.value, tipo_msg="chat_message"))
        nova_msg.value = ""
        page.update()

    def entrar(e):
        if not nome_usuario.value:
            nome_usuario.error_text = "Nome de usuário não pode ficar em branco!"
            nome_usuario.update()
        else:
            page.session.set("nome_usuario", nome_usuario.value)
            page.dialog.open = False
            page.pubsub.send_all(Mensagem(usuario=nome_usuario.value, texto=f"{nome_usuario.value} entrou no chat.", tipo_msg="login_message"))
            page.update()

    chat = ft.Column()
    nova_msg = ft.TextField(label="Digite sua mensagem: ",
    on_submit=enviar)
    nome_usuario = ft.TextField(label="Entre com seu nome de usuário: ")

    page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Column([nome_usuario], tight=True),
        actions=[ft.ElevatedButton(text="Entrar no chat", on_click=entrar)],
        actions_alignment="end"
    )

    page.add(
        ft.Row(
            [ft.Text("Oh Chat!", size=60, weight="bold")],
             alignment=ft.MainAxisAlignment.CENTER  
             ),
        chat,
        ft.Row(
            controls=[nova_msg, ft.ElevatedButton("Enviar",
            on_click=enviar)],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.update()

ft.app(main)
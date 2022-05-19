import win32com.client as win32

# criar a integração com o outlook
outlook = win32.Dispatch('outlook.application')

# criar um email
email = outlook.CreateItem(0)

email1 = str(input("Digite o email do usuário: ")).strip()
senha = str(input('Digite a Senha do usuário: '))
usuario = email1.split('@')

# configurar as informações do seu e-mail
email.To = email1
email.Subject = "Acesso as senhas"
email.HTMLBody = f"""

<h2>Olá, seja bem-vindo(a)</h2>

<h3>Muito sucesso nessa nova jornada</h3>

<p> <strong> Pedimos por gentileza para que leia todo o e-mail </strong> </p> <br>

<ul>
<li><strong> Computador </strong> </li>
<li>Usuário: {usuario[0]} </li>
<li>Senha: Mudar123 </li>
</ul>
<p>------------------------------------------------------------------------</p>
<ul>
<li><strong> Email </strong></li>
<li>Usuário: {email1} </li>
<li>Senha: {senha} </li>
</ul>
<p>------------------------------------------------------------------------</p>
<ul>
<l1><strong> Slack </strong></l1>
<li>Usuário: {email1} </li>
<li>Senha: {senha} </li>
</ul>
<p>------------------------------------------------------------------------</p>
<ul>
<li><strong> Trello </strong></li>
<li>Usuário: {email1} </li>
<li>Senha: {senha} </li>
</ul>
<p>------------------------------------------------------------------------</p>
<pre>Segue também o link do nosso portal de suporte, onde você pode abrir um chamado para solicitações de suporte.
O usuário e senha são os mesmos do computador.</pre>
<p>Sistema de chamados GLPI -><a href="http://suporte.fitcard.com.br/">http://suporte.fitcard.com.br/</a>  </p>
<br><br>
<pre>
Em anexo, estamos enviando um tutorial de como realizar a abertura de chamados.





Qualquer dúvida, estamos à disposição.





Atenciosamente,
</pre>
<img src = "C:\emailauto\infra.png">
"""

anexo = "C:\emailauto\Boas_praticas.pdf"
email.Attachments.Add(anexo)
anexo1 = "C:\emailauto\Sistema_de_abertura_de_Chamado_Fitcard.pdf"
email.Attachments.Add(anexo1)

email.Send()
print("Email Enviado")




<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST['nome'];
    $email = $_POST['email'];
    $mensagem = $_POST['mensagem'];

    $para = "seuemail@floricultura.com";
    $assunto = "Novo contato do site";
    $corpo = "Nome: $nome\nEmail: $email\nMensagem: $mensagem";

    mail($para, $assunto, $corpo);

    echo "Mensagem enviada com sucesso!";
}
?>
<form method="post">
  <input type="text" name="nome" placeholder="Seu nome" required><br>
  <input type="email" name="email" placeholder="Seu email" required><br>
  <textarea name="mensagem" placeholder="Sua mensagem" required></textarea><br>
  <button type="submit">Enviar</button>
</form>

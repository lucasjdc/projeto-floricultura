<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $usuario = $_POST['usuario'];
    $senha = $_POST['senha'];

    // Usuário fixo (pode colocar no banco depois)
    if ($usuario == "admin" && $senha == "1234") {
        $_SESSION['logado'] = true;
        header("Location: dashboard.php");
        exit;
    } else {
    $erro = "Usuário ou senha inválidos!";
    }
} 
?>
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>Login Admin</title></head>
<body>
  <h2>Área Administrativa</h2>
  <?php if (isset($erro)) echo "<p style='color:red'>$erro</p>"; ?>
  <form method="post">
    <input type="text" name="usuario" placeholder="Usuário" required><br>
    <input type="password" name="senha" placeholder="Senha" required><br>
    <button type="submit">Entrar</button>
  </form>
</body>
</html>
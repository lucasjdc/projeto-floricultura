<?php
session_start();
if (!isset($_SESSION['logado'])) {
    header("Location: login.php");
    exit;
}
?>
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>Dashboard</title></head>
<body>
  <h1>Painel Administrativo</h1>
  <p>Bem-vindo ao admin da Floricultura!</p>
  <a href="cadastrar_produto.php">Cadastrar Produto</a> | 
  <a href="../produtos.php">Ver Loja</a> | 
  <a href="logout.php">Sair</a>
</body>
</html>
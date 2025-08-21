<?php
require_once __DIR__ . '/../includes/funcoes.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $estoque = carregarEstoque();

    $estoque[] = [
        "nome" => $_POST['nome'],
        "quantidade" => intval($_POST['quantidade']),
        "preco" =>floatval($_POST['preco'])
    ];

    salvarEstoque($estoque);
    header("Location: index.php");
}
?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">    
    <title>Adicionar Produto</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Adicionar Produto</h1>
    <form method="POST">
        Nome: <input type="text" name="nome" required><br><br>
        Quantidade: <input type="number" name="quantidade" required><br><br>
        Preço (R$): <input type="number" step="0.01" name="preco" required><br><br>
        <button type="submit">Salvar</button>
    </form>
    <br><a href="index.php">Voltar</a>
</body>
</html>
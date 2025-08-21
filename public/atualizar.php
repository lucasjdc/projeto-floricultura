<?php
require_once __DIR__ . '/../includes/funcoes.php';

if (!isset($_GET['i'])) {
    header("Location: index.php");
    exit;
}

$i = intval($_GET['i']);
$estoque = carregarEstoque();

// Verifica se o índice existe
if (!isset($estoque[$i])) {
    header("Location: index.php");
    exit;
}

$produto = $estoque[$i];

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $novaQuantidade = intval($_POST['quantidade']);
    $estoque[$i]['quantidade'] = $novaQuantidade;
    salvarEstoque($estoque);
    header("Location: index.php");
    exit;
}

?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Atualizar Estoque</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Atualizar Estoque - <?= htmlspecialchars($produto['nome']) ?></h1>
    <form method="POST">
        Quantidade atual: <?= $produto['quantidade'] ?><br><br>
        Nova quantidade: <input type="number" name="quantidade" required><br><br>
        <button type="submit">Salvar</button>
    </form>
    <br><a href="index.php">Voltar</a>
</body>
</html>
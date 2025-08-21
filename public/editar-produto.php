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
    $estoque[$i]['nome'] = $_POST['nome'];
    $estoque[$i]['quantidade'] = intval($_POST['quantidade']);
    $estoque[$i]['preco'] = floatval($_POST['preco']);

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
    <h1>Editar Produto - <?= htmlspecialchars($produto['nome']) ?></h1>
    <form method="POST">
        Nome: <input type="text" name="nome" value="<?= htmlspecialchars($produto['nome']) ?>" required><br><br>
        Quantidade: <input type="number" name="quantidade" value="<?= $produto['quantidade'] ?>" required><br><br>
        Preço (R$): <input type="number" step="0.01" name="preco" value="<?= $produto['preco'] ?>" required><br><br>
        <button type="submit">Salvar</button>
    </form>
    <br><a href="index.php">Voltar</a>
</body>
</html>
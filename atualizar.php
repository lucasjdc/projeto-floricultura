<?php
// Esse arquivo abre um formulário para digitar a nova quantidade do produto
$estoque = json_decode(file_get_contents("estoque.json"), true);

if (!isset($_GET['i'])) {
    header("Location: index.php");
    exit;
}

$i = intval($_GET['i']);
$produto = $estoque[$i];

// Se o formulário foi enviado
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $novaQuantidade = intval($_POST['quantidade']);
    $estoque[$i]['quantidade'] = $novaQuantidade;

    file_put_contents("estoque.json", json_encode($estoque, JSON_PRETTY_PRINT));
    header("Location: index.php");
    exit;
}
?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Atualizar Estoque</title>
</head>
<body>
    <h1>Atualizar Estoque - <? $produto['nome'] ?></h1>
    <form method="POST">
        Quantidade atual: <?= $produto['quantidade'] ?><br><br>
        Nova quantidade: <input type="number" name="quantidade" required><br><br>
        <button type="submit">Salvar</button>
    </form>
    <br><a href="index.php">Voltar</a>
</body>
</html>
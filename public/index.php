<?php
require_once __DIR__ . '/../includes/funcoes.php';
$estoque = carregarEstoque();
?>
<!DOCTYPE html>
<html land="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Floricultura - Estoque</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Floricultura - Controle de Estoque</h1>
    <a href="adicionar.php">Adicionar Produto</a>
    <table border="1" cellpadding="5">
        <tr>
            <th>Nome</th>
            <th>Quantidade</th>
            <th>Preço (R$)</th>
            <th>Ações</th>
        </tr>
        <?php foreach ($estoque as $i => $produto): ?>
            <tr>
                <td><?= htmlspecialchars($produto['nome']) ?></td>
                <td><?= $produto['quantidade'] ?></td>
                <td><?= number_format($produto['preco'], 2, ',', '.') ?></td>
                <td>
                    <a href="editar-produto.php?i=<?= $i ?>">Editar Produto</a> |
                    <a href="remover.php?i=<?= $i ?>">Remover Produto</a>
                </td>
            </tr>
        <?php endforeach; ?>
    </table>
</body>
</html>
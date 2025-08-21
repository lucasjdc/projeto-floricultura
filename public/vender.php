<?php
require_once __DIR__ . '/../includes/funcoes.php';

if (isset($_GET['i'])) {
    $i = intval($_GET['i']);
    $estoque = carregarEstoque();

    if ($estoque[$i]['quantidade'] > 0) {
        $estoque[$i]['quantidade'] -= 1;
    }

    salvarEstoque($estoque);
}
header("Location: index.php");
exit;
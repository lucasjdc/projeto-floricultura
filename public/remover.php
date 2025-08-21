<?php
require_once __DIR__ . '/../includes/funcoes.php';

if (isset($_GET['i'])) {
    $estoque = carregarEstoque();
    array_splice($estoque, intval($_GET['i']), 1);
    salvarEstoque($estoque);
}
header("Location: index.php");